# Car Detection and Manufacturer Classification - BA Analysis

## 1. Project Summary
Car Detection and Manufacturer Classification is an incomplete computer vision project that must detect cars in uploaded images and live video, classify detected cars against five trained car manufacturer classes, and present the results in an Angular web UI.

The system will use YOLO for object detection and a ResNet50-based transfer learning CNN classifier for manufacturer prediction. Detected cars will be cropped from the source image or video frame, sent to the classifier, and displayed with bounding boxes and labels. Cars outside the five trained manufacturers must be shown as `Unknown Manufacturer` when confidence is below the accepted threshold.

## 2. Business Goal
Complete a working MVP that demonstrates end-to-end AI-based car detection and manufacturer classification through a web interface.

The project should help DevLab-One prove capability in:
- Computer vision pipelines.
- Object detection plus image classification.
- AI model training and evaluation.
- Django-based AI API services.
- Angular-based AI application UI.
- Future CCTV-style monitoring use cases.

## 3. Target Users
- Security monitoring teams.
- Parking lot operators.
- Building or campus administrators.
- Vehicle inspection teams.
- Demo users evaluating DevLab-One AI capabilities.
- Internal DevLab-One team members validating computer vision delivery.

## 4. Functional Requirements
| ID | Requirement | Priority |
| --- | --- | --- |
| FR-01 | User can upload an image from the Angular UI. | High |
| FR-02 | Backend receives the uploaded image through a Django API. | High |
| FR-03 | YOLO detects objects in the uploaded image. | High |
| FR-04 | System identifies car objects from YOLO results. | High |
| FR-05 | System draws bounding boxes around detected objects. | High |
| FR-06 | System crops each detected car region from the image. | High |
| FR-07 | Each cropped car image is passed to the ResNet50 manufacturer classifier. | High |
| FR-08 | Classifier predicts one of five trained car manufacturers when confidence is sufficient. | High |
| FR-09 | System returns `Unknown Manufacturer` when confidence is below threshold or class is not recognized. | High |
| FR-10 | UI displays processed image with bounding boxes and labels. | High |
| FR-11 | UI displays object label and manufacturer label for each detected car. | High |
| FR-12 | UI supports live camera or video monitoring mode. | Medium |
| FR-13 | Live video mode displays near real-time bounding boxes and labels. | Medium |
| FR-14 | Backend exposes API response data including bounding box coordinates, labels, confidence scores, and processed image reference or encoded output. | High |
| FR-15 | System stores or references the selected best-performing classifier model for inference. | High |
| FR-16 | System design allows adding more manufacturer classes later. | Medium |

## 5. Non-Functional Requirements
| Area | Requirement |
| --- | --- |
| Performance | Image upload inference should return results within an acceptable demo response time, target under 5 seconds for normal image sizes. |
| Live processing | Video mode should support near real-time processing; exact FPS target must be confirmed. |
| Accuracy | Classifier accuracy must be measured on validation and test data before model selection. |
| Reliability | API should handle no-car images, multiple-car images, poor-quality images, and unsupported files gracefully. |
| Security | Uploaded files must be validated by type and size before processing. |
| Scalability | Model and label mapping should support future manufacturer classes without major architecture changes. |
| Maintainability | Detection, cropping, classification, and rendering should be separated into clear backend services/modules. |
| Usability | UI should clearly show upload state, processing state, results, confidence where useful, and errors. |
| Traceability | Training runs should record epoch count, validation accuracy, loss, and selected best model. |

## 6. AI/ML Requirements
- Use YOLO for object detection.
- Detect cars from uploaded images and video frames.
- Crop detected car regions before classification.
- Use transfer learning with ResNet50 architecture for manufacturer classification.
- Train on five manufacturer classes.
- Use at least 200 images per manufacturer.
- Split data into train, validation, and test sets.
- Compare training runs or checkpoints at 10, 20, 30, 40, and 50 epochs.
- Select the best-performing model based on validation/test performance, not only training accuracy.
- Define confidence threshold for known manufacturer prediction.
- Return `Unknown Manufacturer` when prediction confidence is below threshold.
- Save final model artifact, label mapping, preprocessing configuration, and evaluation results.

## 7. Dataset Requirements
| Requirement | Details |
| --- | --- |
| Classes | Five car manufacturer classes, names to be confirmed by CEO. |
| Minimum image count | At least 200 images per manufacturer. |
| Image variety | Include front, rear, side, angled views, different lighting, backgrounds, distances, and car colors. |
| Data quality | Remove duplicates, corrupted files, irrelevant images, and images where manufacturer identity is unclear. |
| Label quality | Folder names or labels must exactly match the five manufacturer names. |
| Split | Recommended 70% train, 15% validation, 15% test, unless dataset size or quality requires adjustment. |
| Unknown class testing | Include non-target manufacturer cars during testing to validate `Unknown Manufacturer` behavior. |
| Preprocessing | Resize and normalize images according to ResNet50 requirements. |
| Augmentation | Use controlled augmentation such as rotation, brightness, zoom, crop, and horizontal flip where appropriate. |

## 8. Training and Validation Plan
1. Confirm the five manufacturer classes.
2. Audit the dataset for quantity, duplicates, quality, and label correctness.
3. Prepare train, validation, and test splits.
4. Apply ResNet50-compatible preprocessing.
5. Train using transfer learning with ResNet50 base model.
6. Run training or evaluate checkpoints at 10, 20, 30, 40, and 50 epochs.
7. Track training accuracy, validation accuracy, training loss, validation loss, and test accuracy.
8. Check overfitting by comparing training and validation curves.
9. Evaluate confusion matrix to identify confused manufacturer classes.
10. Choose the best model using validation accuracy, test accuracy, and stable loss behavior.
11. Define confidence threshold for `Unknown Manufacturer`.
12. Save selected model and evaluation report.

## 9. Accuracy Comparison Plan
| Epoch count | Metrics to capture | Decision use |
| --- | --- | --- |
| 10 | Train accuracy, validation accuracy, loss, confusion matrix snapshot | Early baseline; check if model learns meaningful features. |
| 20 | Train accuracy, validation accuracy, loss, test sample predictions | Compare improvement and early overfitting signs. |
| 30 | Train accuracy, validation accuracy, loss, confusion matrix | Candidate for balanced training duration. |
| 40 | Train accuracy, validation accuracy, loss, test accuracy | Check if extra epochs improve generalization. |
| 50 | Train accuracy, validation accuracy, loss, test accuracy | Final long-run candidate; reject if overfitting increases. |

Model selection rule:
- Prefer the model with the best validation/test performance and stable loss.
- Do not select a model only because training accuracy is highest.
- If two models are close, choose the simpler/earlier epoch model to reduce overfitting risk.

## 10. Backend API Requirements
| API | Purpose | Input | Output |
| --- | --- | --- | --- |
| `POST /api/detect/image/` | Process uploaded image | Image file | Detection results, manufacturer predictions, confidence scores, processed image |
| `POST /api/detect/frame/` | Process one video/camera frame | Image frame | Frame-level detection and classification results |
| `GET /api/model/info/` | Return active model metadata | None | YOLO version, classifier version, class labels, threshold |
| `GET /api/health/` | Confirm service availability | None | Service status |

Expected image result fields:
- Request ID.
- Detected object label.
- Bounding box coordinates.
- Detection confidence.
- Manufacturer label for cars.
- Manufacturer confidence.
- Unknown manufacturer flag.
- Processed image URL or base64 output.
- Error details when processing fails.

Backend rules:
- Validate file type and file size.
- Handle no detected cars.
- Handle multiple detected cars.
- Handle model load failure gracefully.
- Keep model loading efficient so models are not reloaded on every request.
- Log inference errors for debugging.

## 11. Angular UI Requirements
- Image upload page.
- Drag-and-drop or file picker upload.
- Upload validation message for unsupported files.
- Processing/loading state.
- Result view with processed image.
- Bounding boxes visible on detected objects.
- Label display for each detected object.
- Car manufacturer label for recognized manufacturers.
- `Unknown Manufacturer` label for low-confidence or out-of-scope cars.
- Confidence display may be shown if useful for testing/demo.
- Error state for failed upload or failed processing.
- Live monitoring page for camera/video mode.
- Clear navigation between image upload and live monitoring.

## 12. Live Camera/Video Requirements
- UI can access camera feed with user permission.
- UI can send frames to backend for detection/classification.
- Backend processes frames and returns bounding box data.
- UI overlays bounding boxes and labels on the video stream.
- System should support near real-time monitoring.
- FPS target, latency target, and deployment environment must be confirmed.
- Live mode should include start and stop controls.
- Live mode should handle backend delay without freezing the UI.

## 13. User Stories
| ID | User story | Priority |
| --- | --- | --- |
| US-01 | As a user, I want to upload a vehicle image so that I can see detected cars and manufacturer labels. | High |
| US-02 | As a user, I want detected cars to be boxed clearly so that I can understand what the AI found. | High |
| US-03 | As a user, I want recognized cars to show manufacturer names so that I can identify vehicles quickly. | High |
| US-04 | As a user, I want unknown cars to be labeled as unknown so that the system does not show misleading results. | High |
| US-05 | As a user, I want to see results for multiple cars in one image so that group images are supported. | High |
| US-06 | As a user, I want to use a camera feed so that the system can work like CCTV monitoring. | Medium |
| US-07 | As an admin or developer, I want to know which classifier model is active so that I can verify deployment. | Medium |
| US-08 | As the CEO, I want an accuracy comparison across epoch counts so that I can approve the best model for MVP. | High |
| US-09 | As an ML engineer, I want clean dataset rules so that model results are trustworthy. | High |
| US-10 | As a QA tester, I want clear expected behavior for edge cases so that I can validate the application. | High |

## 14. Acceptance Criteria
### Image Upload
- Given a valid image is uploaded, when the user submits it, then the backend processes it and returns detection results.
- Given one or more cars are present, when processing is complete, then each detected car has a bounding box.
- Given a detected car belongs to one of the five trained manufacturers with sufficient confidence, then the UI shows that manufacturer label.
- Given a detected car has low manufacturer confidence, then the UI shows `Unknown Manufacturer`.
- Given no car is detected, then the UI shows a clear no-car-found result.
- Given an invalid file is uploaded, then the UI shows a validation error.

### Model Training
- Given datasets for five manufacturers are available, when training is complete, then results exist for 10, 20, 30, 40, and 50 epochs.
- Given training results are available, when the model is selected, then selection is based on validation/test accuracy and overfitting review.
- Given the best model is selected, then backend inference uses that model.

### Live Monitoring
- Given camera permission is granted, when live mode starts, then the UI displays the camera feed.
- Given cars are visible in the feed, when frames are processed, then bounding boxes and labels appear on the video.
- Given backend processing slows down, then the UI remains usable and does not crash.

## 15. Assumptions
- The five manufacturer datasets are already available or can be provided by the CEO/team.
- Each manufacturer has at least 200 usable images after cleaning.
- YOLO can detect cars accurately enough for the MVP use case.
- ResNet50 transfer learning is acceptable for the first manufacturer classifier.
- Angular and Django are confirmed technology choices.
- Live camera mode can be near real time for MVP; exact FPS is not yet fixed.
- Unknown manufacturer behavior will be based on prediction confidence threshold.
- This project is first a working MVP/demo, not yet a production-grade surveillance platform.

## 16. Risks
| Risk | Impact | Mitigation |
| --- | --- | --- |
| Dataset images are too few or too similar | Poor model accuracy | Audit dataset and add variety before training. |
| Manufacturer classification may confuse visually similar vehicles | Incorrect labels | Use confusion matrix and improve dataset coverage. |
| Unknown manufacturer detection may be unreliable | False known labels | Tune confidence threshold and test with outside manufacturers. |
| YOLO detects cars but crop quality is poor | Classifier accuracy drops | Add crop padding and validate preprocessing. |
| Live video inference may be slow | Poor user experience | Process selected frames, optimize backend, consider GPU. |
| Model overfits at higher epochs | Bad real-world performance | Select model using validation/test performance, not training accuracy. |
| Angular overlay may not align with processed frame dimensions | Incorrect visual results | Standardize image scaling and coordinate mapping. |
| Large uploads may slow or crash backend | Reliability issue | Enforce file size limits and compression rules. |

## 17. Open Questions for CEO
1. What are the five car manufacturer names?
2. Where is the dataset stored, and what is its current folder structure?
3. Should the MVP detect only cars, or should it also show labels for other YOLO-detected objects?
4. What confidence threshold should be acceptable for showing a known manufacturer?
5. Should the UI show confidence percentages to users or only to admins/testers?
6. What is the expected live camera performance target: FPS and maximum delay?
7. Is this intended for demo, internal use, or production deployment?
8. Should images and video frames be stored, or processed without saving?
9. Is GPU infrastructure available for training and/or inference?
10. Should login/authentication be included in MVP?
11. What deployment environment is expected?
12. Should the system support uploaded video files, or only live camera feed and images?

## 18. Recommended Development Phases
### Phase 1: Discovery and Audit
- Confirm five manufacturers.
- Audit dataset quality and class balance.
- Confirm existing incomplete project status.
- Finalize MVP boundaries and success criteria.

### Phase 2: ML Training and Evaluation
- Prepare dataset.
- Train ResNet50 classifier.
- Compare 10, 20, 30, 40, and 50 epoch results.
- Select best model.
- Define unknown threshold.

### Phase 3: Backend API
- Build Django APIs for image upload and frame processing.
- Integrate YOLO detection.
- Integrate classifier inference.
- Return structured detection and classification results.

### Phase 4: Angular UI
- Build image upload flow.
- Build result display with bounding boxes and labels.
- Build live camera monitoring view.

### Phase 5: QA and Demo Readiness
- Test with single-car, multi-car, no-car, unknown manufacturer, and poor-quality images.
- Validate API performance and error handling.
- Prepare demo dataset and final handoff notes.

## 19. Required AI/Software Team Roles
| Role | Responsibility | Usage |
| --- | --- | --- |
| Business Analyst | Requirements, scope, acceptance criteria, CEO clarification | Part-time |
| Project Manager | Plan phases, track delivery, coordinate team | Part-time |
| Solution Architect | Overall architecture, API/model integration design | Part-time |
| ML Engineer | Dataset prep, YOLO integration, ResNet50 training, evaluation | Full-time during ML phase |
| Backend Developer | Django APIs, model loading, inference services | Full-time during backend phase |
| Frontend Developer | Angular upload UI, result UI, live camera UI | Full-time during UI phase |
| UX Designer | User flow and result presentation | Part-time |
| QA Engineer | Test plan, edge cases, acceptance validation | Part-time |
| DevOps Engineer | Environment, deployment, model artifact handling | Review/part-time |
| Security Engineer | Upload security, storage decisions, API review | Review only |
| Documentation | Setup guide, API notes, model evaluation summary | Part-time |

## 20. MVP Scope and Future Scope
### MVP Scope
- Five manufacturer classes.
- YOLO car detection from uploaded images.
- Crop detected cars and classify manufacturer.
- Unknown manufacturer label using confidence threshold.
- Django image processing API.
- Angular image upload and result display.
- Accuracy comparison for 10, 20, 30, 40, and 50 epochs.
- Basic live camera monitoring with bounding boxes and labels if performance allows.

### Future Scope
- Add more manufacturers.
- Add specific car model classification.
- Support uploaded video files.
- Improve live CCTV performance.
- Add authentication and user roles.
- Add detection history and search.
- Add dashboard analytics for vehicle counts and manufacturer frequency.
- Add production deployment with GPU acceleration.
- Add retraining workflow for new classes.

## BA Recommendation
Proceed with structured discovery and technical audit before implementation. The next CEO decision should confirm the five manufacturer names, dataset location, MVP performance expectations, and whether live video is mandatory for the first MVP release or can be a Phase 2 enhancement.
