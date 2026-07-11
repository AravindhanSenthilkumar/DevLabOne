# Machine Learning

## Purpose
This folder contains the car detection and manufacturer classification ML work.

## Planned Pipeline
1. Use YOLO to detect cars in source images or video frames.
2. Crop each detected car region.
3. Train a ResNet50 transfer learning classifier on five manufacturer folders.
4. Compare model performance at 10, 20, 30, 40, and 50 epochs.
5. Select the best model based on validation and test accuracy.
6. Use confidence thresholding to return `Unknown Manufacturer` for out-of-scope cars.

## Folders
- `datasets`: raw and processed image datasets.
- `models/yolo`: YOLO model files or references.
- `models/classifier`: trained ResNet50 classifier artifacts.
- `scripts`: training, evaluation, preprocessing, and inference scripts.
- `notebooks`: experiments and analysis.
- `reports`: dataset audit and model evaluation reports.
