# Backend Django API

## Purpose
This folder will contain the Django API service.

## Planned APIs
- `POST /api/detect/image/`
- `POST /api/detect/frame/`
- `GET /api/model/info/`
- `GET /api/health/`

## Responsibilities
- Validate uploaded images and frames.
- Run YOLO detection.
- Crop detected cars.
- Run ResNet50 manufacturer classifier.
- Return bounding boxes, object labels, manufacturer labels, and confidence scores.
