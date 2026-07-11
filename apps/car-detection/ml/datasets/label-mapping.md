# Label Mapping

## Current Dataset Source
`/Users/aravindhansenthilkumar/Documents/DevLab-One/apps/car-detection/tests/sample-images`

## Folder to Manufacturer Mapping
| Folder Name | Manufacturer Label | Current Image Count |
| --- | --- | --- |
| `Audi S6 Sedan 2011` | `Audi` | 92 |
| `BMW X6 SUV 2012` | `BMW` | 84 |
| `Jeep Compass SUV 2012` | `Jeep` | 85 |
| `Suzuki SX4 Sedan 2012` | `Suzuki` | 80 |
| `Tesla Model S Sedan 2012` | `Tesla` | 77 |

## Training Label Rule
For the MVP, train the classifier with manufacturer labels:

- Audi
- BMW
- Jeep
- Suzuki
- Tesla

The source folder names include model and year, but the UI should show only the manufacturer label unless the CEO later approves model-level classification.

## Known Limitation
Each class currently has fewer than the target minimum of 200 images. This is acceptable for a prototype training run, but the ML Engineer should report accuracy risk and recommend adding more images before production use.
