# Decision Log

Record important company, product, architecture, security, and delivery decisions here.

## Format

### YYYY-MM-DD - Decision Title
- Status: Proposed | Accepted | Rejected | Superseded
- Context:
- Decision:
- Consequences:
- Owner:

## Decisions

### 2026-07-10 - Car Detection Selected as Active Project
- Status: Accepted
- Context: CEO confirmed that DevLab-One already has an incomplete project idea named Car Detection that must be completed before continuing general idea discovery.
- Decision: Make Car Detection and Manufacturer Classification the active DevLab-One project.
- Consequences: Company workflow shifts from project idea discovery to MVP planning and execution for YOLO detection, ResNet50 manufacturer classification, Django API, and Angular UI.
- Owner: CEO

### 2026-07-10 - Car Detection Initial Technical Direction
- Status: Accepted
- Context: CEO specified YOLO object detection, cropped car images, ResNet50 transfer learning classifier, five manufacturer classes, Django backend, and Angular frontend.
- Decision: Use YOLO for object detection, ResNet50 for manufacturer classification, Django for API services, and Angular for UI.
- Consequences: DevLab-One needs ML Engineer ownership, dataset audit, model training comparison at 10/20/30/40/50 epochs, API integration, and UI implementation.
- Owner: CEO

### 2026-07-11 - Maintain Local MVP Setup for Further Development
- Status: Accepted
- Context: CEO decided on deployment options and chose to keep the application locally for further feature enhancements rather than deploying it immediately.
- Decision: Postpone Hugging Face and Vercel cloud deployments. Maintain active local development servers for addition of new features.
- Consequences: Focus will be on local prototyping, additional visual components, advanced model refinements, or mock data streams.
- Owner: CEO
