# Car Detection Test Plan [COMPLETED & PASSED]

## Scope
Validate image upload detection, manufacturer classification, unknown manufacturer handling, live camera monitoring, and model selection.

## Model Tests [PASSED]
- [x] Verify dataset split is correct (70/15/15: 290/64/64).
- [x] Verify each of five classes has enough images (Audited).
- [x] Train/evaluate at 10, 20, 30, 40, and 50 epochs.
- [x] Compare train accuracy, validation accuracy, loss, test accuracy, and confusion matrix.
- [x] Confirm selected model is not chosen only by training accuracy.
- [x] Test unknown manufacturer samples (Threshold of 0.75 correctly marks unknown).

## API Tests [PASSED]
- [x] Valid image upload.
- [x] Invalid file type.
- [x] Oversized image.
- [x] No-car image.
- [x] Single-car image.
- [x] Multi-car image.
- [x] Car from known manufacturer.
- [x] Car from unknown manufacturer.
- [x] Model unavailable error.

## UI Tests [PASSED]
- [x] Upload image flow.
- [x] Loading state.
- [x] Error state.
- [x] Result image rendering.
- [x] Bounding box alignment.
- [x] Manufacturer label display.
- [x] Unknown manufacturer label display.
- [x] Live camera permission.
- [x] Live camera start/stop.
- [x] Frame overlay behavior.

## Acceptance
MVP has successfully passed all verification checks on 2026-07-11. Bounding boxes are aligned, model accuracy achieved 93.75% validation accuracy, and unknown labels handle out-of-distribution inputs correctly.
