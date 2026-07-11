# Car Detection Dataset

## Raw Dataset
Paste original manufacturer images into `raw`.

Expected structure:

```text
raw/
  manufacturer-1/
  manufacturer-2/
  manufacturer-3/
  manufacturer-4/
  manufacturer-5/
```

Rules:
- One manufacturer per folder.
- Minimum 200 usable images per manufacturer.
- Use clear manufacturer folder names after the CEO confirms the five brands.
- Remove duplicate, corrupted, blurry, unrelated, or unclear images before training.
- Include different angles, colors, lighting, distances, and backgrounds.

## Processed Dataset
The ML Engineer will later create:

```text
processed/
  train/
  validation/
  test/
```

Do not paste raw images directly into `processed`. It will be generated from the raw dataset.
