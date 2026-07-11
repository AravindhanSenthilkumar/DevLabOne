# Car Detection Architecture

## Project
Car Detection and Manufacturer Classification.

## Goal
Detect cars in uploaded images and live camera frames, crop detected car regions, classify manufacturer using a ResNet50 transfer learning model trained on five manufacturers, and return labeled bounding boxes to the Angular UI.

## System Components
- Angular UI: image upload, result display, live camera monitoring.
- Django API: upload endpoint, frame endpoint, model metadata endpoint, health endpoint.
- YOLO detector: detects cars and provides bounding boxes.
- Crop service: extracts car regions from images or frames.
- ResNet50 classifier: predicts one of five trained manufacturers.
- Unknown threshold logic: returns `Unknown Manufacturer` when confidence is too low.
- Result renderer: returns bounding box data and optionally processed image output.

## Inference Flow
1. User uploads image or sends camera frame from Angular.
2. Django validates file type and size.
3. YOLO detects objects.
4. Backend filters car detections.
5. Backend crops each car region with safe padding.
6. ResNet50 classifier predicts manufacturer for each crop.
7. Confidence threshold decides known manufacturer or `Unknown Manufacturer`.
8. API returns bounding boxes, labels, confidence values, and processed image reference or encoded image.
9. Angular displays labels and overlays bounding boxes.

## Training Flow
1. Confirm five manufacturer names.
2. Audit dataset with minimum 200 images per class.
3. Clean duplicates, corrupted files, and unclear labels.
4. Split into train, validation, and test datasets.
5. Apply ResNet50 preprocessing and controlled augmentation.
6. Train/evaluate at 10, 20, 30, 40, and 50 epochs.
7. Compare validation/test accuracy, loss, and confusion matrix.
8. Select best model.
9. Save model, labels, threshold, and evaluation report.

## API Endpoints
- `POST /api/detect/image/`
- `POST /api/detect/frame/`
- `GET /api/model/info/`
- `GET /api/health/`

## MVP Architecture Decision
Use Angular for frontend and Django for backend. Keep detection, cropping, classification, and response formatting as separate backend modules.
