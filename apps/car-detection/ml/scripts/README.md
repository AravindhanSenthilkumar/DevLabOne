# ML Scripts

## Train ResNet50 Classifier

The training script uses the current manufacturer folders in:

`apps/car-detection/tests/sample-images`

It applies training-time augmentation:

- Random resized crop.
- Horizontal flip.
- Small rotation.
- Brightness, contrast, and saturation jitter.
- ImageNet normalization.

Run:

```bash
python3 apps/car-detection/ml/scripts/train_resnet50_classifier.py --pretrained --freeze-backbone
```

The script saves:

- Checkpoints at 10, 20, 30, 40, and 50 epochs.
- Best selected model.
- Label mapping.
- Training metrics CSV.
- Training report JSON.

If pretrained ImageNet weights are not available locally, the first run needs network access to download them.
