# Car Detection Project

This project detects cars in images or video frames using YOLO, crops detected car regions, and classifies each car manufacturer using a ResNet50 transfer learning classifier trained on five manufacturer classes.

## Main Folders
- `frontend-angular`: Angular UI for image upload, results, and live camera monitoring.
- `backend-django`: Django API service for detection and classification.
- `ml`: Dataset, training scripts, model artifacts, notebooks, and reports.
- `api-contracts`: API request and response contracts.
- `tests`: Test images and validation assets.
- `uploads`: Temporary uploaded files during local development.
- `outputs`: Processed images, cropped cars, and video frames.

## Dataset Location
Paste manufacturer photos into:

- `ml/datasets/raw/manufacturer-1`
- `ml/datasets/raw/manufacturer-2`
- `ml/datasets/raw/manufacturer-3`
- `ml/datasets/raw/manufacturer-4`
- `ml/datasets/raw/manufacturer-5`

Each folder should contain at least 200 images for one manufacturer.

After you confirm the five manufacturer names, rename these folders to the real names.
