# Known Issues

Track accepted, deferred, or under-investigation issues.

## Format

### Issue Title
- Status:
- Severity:
- Area:
- Impact:
- Workaround:
- Owner:
- Target fix:

## Issues

### Car Detection Dataset Below Target Count
- Status: Open
- Severity: Medium
- Area: Machine Learning
- Impact: Classifier accuracy may not generalize well because each class has fewer than the target minimum of 200 images and appears to represent one model/year per manufacturer.
- Workaround: Proceed with prototype training to validate the pipeline, but mark accuracy as prototype-only until more varied images are added.
- Owner: ML Engineer
- Target fix: Add more images per manufacturer before production-quality model selection.
