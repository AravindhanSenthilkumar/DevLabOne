# Dataset Audit - 2026-07-10

## Project
Car Detection and Manufacturer Classification.

## Dataset Location
`/Users/aravindhansenthilkumar/Documents/DevLab-One/apps/car-detection/tests/sample-images`

## Summary
The CEO provided five image folders for the first classifier dataset. Folder names indicate car model/year, and each folder maps to one manufacturer.

## Class Counts
| Folder | Manufacturer | Image Count | Meets 200 Image Target? |
| --- | --- | ---: | --- |
| `Audi S6 Sedan 2011` | Audi | 92 | No |
| `BMW X6 SUV 2012` | BMW | 84 | No |
| `Jeep Compass SUV 2012` | Jeep | 85 | No |
| `Suzuki SX4 Sedan 2012` | Suzuki | 80 | No |
| `Tesla Model S Sedan 2012` | Tesla | 77 | No |

## Findings
- Five target classes are available.
- The current dataset is enough to start a prototype training pipeline.
- The current dataset is below the original 200-image-per-class target.
- Because each class appears to contain one model/year, the model may learn model-specific features instead of general manufacturer features.
- Accuracy must be treated as prototype accuracy until more diverse images are added.

## Recommendation
Proceed with a prototype training run to validate the pipeline:

1. Use the current dataset as the first training source.
2. Split into train, validation, and test sets.
3. Train/evaluate ResNet50 at 10, 20, 30, 40, and 50 epochs.
4. Report accuracy and overfitting risk clearly.
5. Add more varied images later for better manufacturer-level classification.

## Risk Level
Medium.

Reason: The pipeline can be built, but manufacturer accuracy may not generalize well with fewer than 200 images per class and only one model/year per manufacturer.
