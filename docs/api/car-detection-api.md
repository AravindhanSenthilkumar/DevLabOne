# Car Detection API Design

## POST /api/detect/image/

Purpose: Process one uploaded image and return car/object detection results.

### Request
- Multipart form field: `image`

### Response
```json
{
  "requestId": "string",
  "imageWidth": 1280,
  "imageHeight": 720,
  "processedImage": "string",
  "detections": [
    {
      "objectLabel": "car",
      "detectionConfidence": 0.94,
      "box": {
        "x": 120,
        "y": 80,
        "width": 300,
        "height": 180
      },
      "manufacturerLabel": "Toyota",
      "manufacturerConfidence": 0.91,
      "unknownManufacturer": false
    }
  ]
}
```

## POST /api/detect/frame/

Purpose: Process one camera/video frame and return detection overlays for live monitoring.

### Request
- Multipart form field: `frame`
- Optional field: `sessionId`

### Response
Same detection format as image endpoint.

## GET /api/model/info/

Purpose: Return active model metadata.

### Response
```json
{
  "detector": "YOLO",
  "classifier": "ResNet50 transfer learning",
  "manufacturers": ["TBD"],
  "unknownThreshold": 0.75,
  "selectedEpoch": 0,
  "modelVersion": "TBD"
}
```

## GET /api/health/

Purpose: Confirm API service is running.

### Response
```json
{
  "status": "ok"
}
```

## Validation Rules
- Accept only supported image formats.
- Enforce maximum file size.
- Return clear errors for invalid files, no car detected, model unavailable, and processing failure.
