#!/usr/bin/env python3
"""Train a ResNet50 manufacturer classifier for the car detection project."""

from __future__ import annotations

import argparse
import csv
import json
import random
import time
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
import torch
from PIL import Image
from torch import nn, optim
from torch.utils.data import DataLoader, Dataset, Subset
from torchvision import models, transforms
from torchvision.datasets import ImageFolder


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


MANUFACTURER_LABELS = {
    "Audi S6 Sedan 2011": "Audi",
    "BMW X6 SUV 2012": "BMW",
    "Jeep Compass SUV 2012": "Jeep",
    "Suzuki SX4 Sedan 2012": "Suzuki",
    "Tesla Model S Sedan 2012": "Tesla",
}


@dataclass
class EpochMetrics:
    epoch: int
    train_loss: float
    train_accuracy: float
    validation_loss: float
    validation_accuracy: float
    test_loss: float | None = None
    test_accuracy: float | None = None


class TransformSubset(Dataset):
    def __init__(self, subset: Subset, transform) -> None:
        self.subset = subset
        self.transform = transform
        self.dataset = subset.dataset

    def __len__(self) -> int:
        return len(self.subset)

    def __getitem__(self, index: int):
        path, label = self.dataset.samples[self.subset.indices[index]]
        image = Image.open(path).convert("RGB")
        return self.transform(image), label


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data-dir",
        default="apps/car-detection/tests/sample-images",
        help="Folder containing one subfolder per class.",
    )
    parser.add_argument(
        "--output-dir",
        default="apps/car-detection/ml/models/classifier",
        help="Folder where model checkpoints and metadata will be written.",
    )
    parser.add_argument(
        "--report-dir",
        default="apps/car-detection/ml/reports/training-runs",
        help="Folder where training metrics will be written.",
    )
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--learning-rate", type=float, default=0.0003)
    parser.add_argument("--weight-decay", type=float, default=0.0001)
    parser.add_argument("--max-epochs", type=int, default=50)
    parser.add_argument("--checkpoint-epochs", default="10,20,30,40,50")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--pretrained",
        action="store_true",
        help="Use ImageNet pretrained ResNet50 weights. Requires cached weights or network access.",
    )
    parser.add_argument(
        "--freeze-backbone",
        action="store_true",
        help="Freeze ResNet50 backbone and train only the classifier head.",
    )
    return parser.parse_args()


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def validate_dataset(data_dir: Path) -> None:
    if not data_dir.exists():
        raise FileNotFoundError(f"Dataset folder not found: {data_dir}")

    class_dirs = [p for p in data_dir.iterdir() if p.is_dir()]
    if len(class_dirs) != 5:
        raise ValueError(f"Expected 5 class folders, found {len(class_dirs)} in {data_dir}")

    for class_dir in sorted(class_dirs):
        image_count = sum(1 for p in class_dir.iterdir() if p.suffix.lower() in IMAGE_EXTENSIONS)
        if image_count == 0:
            raise ValueError(f"No supported images found in {class_dir}")


def make_splits(dataset: ImageFolder, seed: int) -> tuple[Subset, Subset, Subset]:
    train_indices: list[int] = []
    validation_indices: list[int] = []
    test_indices: list[int] = []
    rng = random.Random(seed)

    by_class: dict[int, list[int]] = {class_idx: [] for class_idx in range(len(dataset.classes))}
    for index, (_, class_idx) in enumerate(dataset.samples):
        by_class[class_idx].append(index)

    for indices in by_class.values():
        rng.shuffle(indices)
        count = len(indices)
        train_end = max(1, int(count * 0.7))
        validation_end = max(train_end + 1, int(count * 0.85))
        validation_end = min(validation_end, count - 1)
        train_indices.extend(indices[:train_end])
        validation_indices.extend(indices[train_end:validation_end])
        test_indices.extend(indices[validation_end:])

    return Subset(dataset, train_indices), Subset(dataset, validation_indices), Subset(dataset, test_indices)


def build_transforms() -> tuple[transforms.Compose, transforms.Compose]:
    train_transform = transforms.Compose(
        [
            transforms.Resize((256, 256)),
            transforms.RandomResizedCrop(224, scale=(0.75, 1.0)),
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.RandomRotation(degrees=12),
            transforms.ColorJitter(brightness=0.25, contrast=0.25, saturation=0.2),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
    eval_transform = transforms.Compose(
        [
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
    return train_transform, eval_transform


def build_model(class_count: int, pretrained: bool, freeze_backbone: bool) -> nn.Module:
    if pretrained:
        weights = models.ResNet50_Weights.DEFAULT
        model = models.resnet50(weights=weights)
    else:
        model = models.resnet50(weights=None)

    if freeze_backbone:
        for parameter in model.parameters():
            parameter.requires_grad = False

    input_features = model.fc.in_features
    model.fc = nn.Sequential(
        nn.Dropout(p=0.35),
        nn.Linear(input_features, class_count),
    )
    return model


def run_epoch(model, loader, criterion, device, optimizer=None) -> tuple[float, float]:
    is_training = optimizer is not None
    model.train(is_training)
    total_loss = 0.0
    correct = 0
    total = 0

    for images, labels in loader:
        images = images.to(device)
        labels = labels.to(device)

        if is_training:
            optimizer.zero_grad(set_to_none=True)

        with torch.set_grad_enabled(is_training):
            outputs = model(images)
            loss = criterion(outputs, labels)
            if is_training:
                loss.backward()
                optimizer.step()

        total_loss += loss.item() * images.size(0)
        predictions = outputs.argmax(dim=1)
        correct += (predictions == labels).sum().item()
        total += labels.size(0)

    return total_loss / max(total, 1), correct / max(total, 1)


def confusion_matrix(model, loader, class_count: int, device) -> list[list[int]]:
    matrix = [[0 for _ in range(class_count)] for _ in range(class_count)]
    model.eval()
    with torch.no_grad():
        for images, labels in loader:
            images = images.to(device)
            outputs = model(images)
            predictions = outputs.argmax(dim=1).cpu().tolist()
            for actual, predicted in zip(labels.tolist(), predictions):
                matrix[actual][predicted] += 1
    return matrix


def save_checkpoint(model, output_dir: Path, epoch: int, metrics: EpochMetrics) -> Path:
    checkpoint_path = output_dir / "checkpoints" / f"resnet50_epoch_{epoch}.pt"
    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(
        {
            "epoch": epoch,
            "model_state_dict": model.state_dict(),
            "metrics": asdict(metrics),
        },
        checkpoint_path,
    )
    return checkpoint_path


def main() -> None:
    args = parse_args()
    set_seed(args.seed)

    data_dir = Path(args.data_dir)
    output_dir = Path(args.output_dir)
    report_dir = Path(args.report_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)

    validate_dataset(data_dir)

    base_dataset = ImageFolder(data_dir)
    train_subset, validation_subset, test_subset = make_splits(base_dataset, args.seed)
    train_transform, eval_transform = build_transforms()

    train_dataset = TransformSubset(train_subset, train_transform)
    validation_dataset = TransformSubset(validation_subset, eval_transform)
    test_dataset = TransformSubset(test_subset, eval_transform)

    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True, num_workers=0)
    validation_loader = DataLoader(validation_dataset, batch_size=args.batch_size, shuffle=False, num_workers=0)
    test_loader = DataLoader(test_dataset, batch_size=args.batch_size, shuffle=False, num_workers=0)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    checkpoint_epochs = {int(value.strip()) for value in args.checkpoint_epochs.split(",") if value.strip()}
    model = build_model(len(base_dataset.classes), args.pretrained, args.freeze_backbone).to(device)

    trainable_parameters = [parameter for parameter in model.parameters() if parameter.requires_grad]
    optimizer = optim.AdamW(trainable_parameters, lr=args.learning_rate, weight_decay=args.weight_decay)
    criterion = nn.CrossEntropyLoss()

    folder_labels = {str(index): class_name for index, class_name in enumerate(base_dataset.classes)}
    manufacturer_labels = {
        str(index): MANUFACTURER_LABELS.get(class_name, class_name)
        for index, class_name in enumerate(base_dataset.classes)
    }

    metadata = {
        "data_dir": str(data_dir),
        "classes": folder_labels,
        "manufacturer_labels": manufacturer_labels,
        "train_count": len(train_dataset),
        "validation_count": len(validation_dataset),
        "test_count": len(test_dataset),
        "device": str(device),
        "pretrained": args.pretrained,
        "freeze_backbone": args.freeze_backbone,
        "augmentation": [
            "resize 256x256",
            "random resized crop 224",
            "horizontal flip",
            "rotation 12 degrees",
            "color jitter",
            "ImageNet normalization",
        ],
    }
    (output_dir / "label_mapping.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    print(f"Training on {device}")
    print(f"Classes: {manufacturer_labels}")
    print(f"Split: train={len(train_dataset)}, validation={len(validation_dataset)}, test={len(test_dataset)}")

    metrics: list[EpochMetrics] = []
    start_time = time.time()

    for epoch in range(1, args.max_epochs + 1):
        train_loss, train_accuracy = run_epoch(model, train_loader, criterion, device, optimizer)
        validation_loss, validation_accuracy = run_epoch(model, validation_loader, criterion, device)
        epoch_metrics = EpochMetrics(
            epoch=epoch,
            train_loss=train_loss,
            train_accuracy=train_accuracy,
            validation_loss=validation_loss,
            validation_accuracy=validation_accuracy,
        )
        metrics.append(epoch_metrics)

        print(
            f"epoch={epoch:02d} "
            f"train_acc={train_accuracy:.4f} val_acc={validation_accuracy:.4f} "
            f"train_loss={train_loss:.4f} val_loss={validation_loss:.4f}"
        )

        if epoch in checkpoint_epochs:
            test_loss, test_accuracy = run_epoch(model, test_loader, criterion, device)
            epoch_metrics.test_loss = test_loss
            epoch_metrics.test_accuracy = test_accuracy
            save_checkpoint(model, output_dir, epoch, epoch_metrics)
            print(f"checkpoint epoch={epoch:02d} test_acc={test_accuracy:.4f} test_loss={test_loss:.4f}")

    completed_checkpoints = [metric for metric in metrics if metric.epoch in checkpoint_epochs]
    best_metric = max(
        completed_checkpoints,
        key=lambda item: (
            item.validation_accuracy,
            item.test_accuracy if item.test_accuracy is not None else 0.0,
            -item.validation_loss,
        ),
    )

    best_checkpoint = output_dir / "checkpoints" / f"resnet50_epoch_{best_metric.epoch}.pt"
    final_model_path = output_dir / "best_resnet50_classifier.pt"
    torch.save(
        {
            "epoch": best_metric.epoch,
            "model_state_dict": torch.load(best_checkpoint, map_location="cpu")["model_state_dict"],
            "metrics": asdict(best_metric),
            "metadata": metadata,
        },
        final_model_path,
    )

    metrics_csv = report_dir / "resnet50_training_metrics.csv"
    with metrics_csv.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(asdict(metrics[0]).keys()))
        writer.writeheader()
        for metric in metrics:
            writer.writerow(asdict(metric))

    matrix = confusion_matrix(model, test_loader, len(base_dataset.classes), device)
    report = {
        "elapsed_seconds": round(time.time() - start_time, 2),
        "best_epoch": best_metric.epoch,
        "best_metrics": asdict(best_metric),
        "metadata": metadata,
        "test_confusion_matrix": matrix,
        "metrics_csv": str(metrics_csv),
        "best_model": str(final_model_path),
    }
    (report_dir / "resnet50_training_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"Best epoch: {best_metric.epoch}")
    print(f"Best model: {final_model_path}")
    print(f"Report: {report_dir / 'resnet50_training_report.json'}")


if __name__ == "__main__":
    main()
