import os
import cv2
import json
import torch
import numpy as np
from PIL import Image
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.files.storage import default_storage

# Try importing ultralytics and torchvision models
try:
    from ultralytics import YOLO
    YOLO_AVAILABLE = True
except ImportError:
    YOLO_AVAILABLE = False

from torchvision import models, transforms
import torch.nn as nn

# Paths for models and mappings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLASSIFIER_PATH = os.path.join(BASE_DIR, '../ml/models/classifier/best_resnet50_classifier.pt')
LABEL_MAPPING_PATH = os.path.join(BASE_DIR, '../ml/models/classifier/label_mapping.json')

# Cache for loaded models to prevent reloading on each request
_yolo_model = None
_classifier_model = None
_label_mapping = None

def get_yolo_model():
    global _yolo_model
    if _yolo_model is None and YOLO_AVAILABLE:
        # Load yolov8n.pt (downloads automatically if not cached)
        _yolo_model = YOLO("yolov8n.pt")
    return _yolo_model

def get_label_mapping():
    global _label_mapping
    if _label_mapping is None:
        if os.path.exists(LABEL_MAPPING_PATH):
            try:
                with open(LABEL_MAPPING_PATH, 'r', encoding='utf-8') as f:
                    _label_mapping = json.load(f)
            except Exception:
                pass
        if _label_mapping is None:
            # Fallback labels
            _label_mapping = {
                "manufacturer_labels": {
                    "0": "Audi",
                    "1": "BMW",
                    "2": "Jeep",
                    "3": "Suzuki",
                    "4": "Tesla"
                }
            }
    return _label_mapping

def get_classifier_model(num_classes=5):
    global _classifier_model
    if _classifier_model is None:
        if os.path.exists(CLASSIFIER_PATH):
            try:
                # Reconstruct ResNet50 classifier head structure
                model = models.resnet50(weights=None)
                input_features = model.fc.in_features
                model.fc = nn.Sequential(
                    nn.Dropout(p=0.35),
                    nn.Linear(input_features, num_classes),
                )
                
                # Load weights
                checkpoint = torch.load(CLASSIFIER_PATH, map_location='cpu')
                model.load_state_dict(checkpoint['model_state_dict'])
                model.eval()
                _classifier_model = model
            except Exception as e:
                print(f"Error loading classifier model: {e}")
    return _classifier_model

def classify_cropped_image(crop_img):
    """Run ResNet50 classification on a cropped image."""
    model = get_classifier_model()
    mapping = get_label_mapping()
    
    if model is None:
        # Fallback/mock prediction if classifier is not trained yet
        return "Unknown Manufacturer", 0.0, True

    # Preprocess crop_img for ResNet50
    try:
        # Convert OpenCV image (BGR) to PIL Image (RGB)
        crop_rgb = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(crop_rgb)
        
        eval_transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        
        input_tensor = eval_transform(pil_img).unsqueeze(0)
        with torch.no_grad():
            outputs = model(input_tensor)
            probabilities = torch.softmax(outputs, dim=1)[0]
            max_idx = torch.argmax(probabilities).item()
            confidence = probabilities[max_idx].item()
            
        manufacturer_labels = mapping.get("manufacturer_labels", {})
        predicted_label = manufacturer_labels.get(str(max_idx), "Unknown")
        
        # Check against threshold (0.75)
        if confidence >= 0.75:
            return predicted_label, round(confidence, 4), False
        else:
            return "Unknown Manufacturer", round(confidence, 4), True
    except Exception as e:
        print(f"Error in classification inference: {e}")
        return "Unknown Manufacturer", 0.0, True

class HealthView(APIView):
    def get(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)

class ModelInfoView(APIView):
    def get(self, request):
        mapping = get_label_mapping()
        classifier_exists = os.path.exists(CLASSIFIER_PATH)
        
        manufacturers = list(mapping.get("manufacturer_labels", {}).values())
        selected_epoch = 0
        if classifier_exists:
            try:
                checkpoint = torch.load(CLASSIFIER_PATH, map_location='cpu')
                selected_epoch = checkpoint.get('epoch', 0)
            except Exception:
                pass
                
        return Response({
            "detector": "YOLOv8",
            "classifier": "ResNet50 transfer learning",
            "manufacturers": manufacturers,
            "unknownThreshold": 0.75,
            "selectedEpoch": selected_epoch,
            "modelVersion": "resnet50_v1" if classifier_exists else "untrained"
        }, status=status.HTTP_200_OK)

class DetectImageView(APIView):
    def post(self, request):
        if 'image' not in request.FILES:
            return Response({"error": "No image file provided"}, status=status.HTTP_400_BAD_REQUEST)
            
        image_file = request.FILES['image']
        
        # Basic extension validation
        ext = os.path.splitext(image_file.name)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png', '.webp', '.bmp']:
            return Response({"error": "Unsupported image format"}, status=status.HTTP_400_BAD_REQUEST)

        # Save uploaded file temporarily
        temp_path = default_storage.save(f"uploads/{image_file.name}", image_file)
        full_temp_path = os.path.join(settings.MEDIA_ROOT, temp_path)
        
        try:
            # Read image using OpenCV
            img = cv2.imread(full_temp_path)
            if img is None:
                return Response({"error": "Failed to read image file"}, status=status.HTTP_400_BAD_REQUEST)
                
            height, width, _ = img.shape
            
            # Run YOLO Detection
            yolo = get_yolo_model()
            detections = []
            
            if yolo is not None:
                results = yolo(img)
                # Filter class 2 (car) in COCO dataset
                for result in results:
                    boxes = result.boxes
                    for box in boxes:
                        cls_id = int(box.cls[0].item())
                        # COCO classes: 2 = car, 5 = bus, 7 = truck
                        if cls_id in [2, 5, 7]:
                            detect_conf = float(box.conf[0].item())
                            xyxy = box.xyxy[0].cpu().numpy().astype(int)
                            x_min, y_min, x_max, y_max = xyxy
                            
                            # Crop region with 10% padding
                            w = x_max - x_min
                            h = y_max - y_min
                            pad_x = int(w * 0.1)
                            pad_y = int(h * 0.1)
                            
                            x_min_pad = max(0, x_min - pad_x)
                            y_min_pad = max(0, y_min - pad_y)
                            x_max_pad = min(width, x_max + pad_x)
                            y_max_pad = min(height, y_max + pad_y)
                            
                            crop = img[y_min_pad:y_max_pad, x_min_pad:x_max_pad]
                            
                            # Classify cropped car image
                            manufacturer_label = "Unknown Manufacturer"
                            manufacturer_conf = 0.0
                            is_unknown = True
                            
                            if crop.size > 0:
                                manufacturer_label, manufacturer_conf, is_unknown = classify_cropped_image(crop)
                            
                            # Save processed bounding box details
                            detections.append({
                                "objectLabel": "car" if cls_id == 2 else ("bus" if cls_id == 5 else "truck"),
                                "detectionConfidence": round(detect_conf, 4),
                                "box": {
                                    "x": int(x_min),
                                    "y": int(y_min),
                                    "width": int(w),
                                    "height": int(h)
                                },
                                "manufacturerLabel": manufacturer_label,
                                "manufacturerConfidence": manufacturer_conf,
                                "unknownManufacturer": is_unknown
                            })
                            
                            # Draw bounding boxes and labels on output image
                            label_str = f"{manufacturer_label} ({int(manufacturer_conf * 100)}%)" if not is_unknown else "Unknown"
                            color = (0, 165, 255) if is_unknown else (0, 200, 80) # Amber vs Emerald
                            cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color, 3)
                            cv2.putText(img, label_str, (x_min, max(15, y_min - 10)),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            
            # Save processed image to media/outputs
            os.makedirs(os.path.join(settings.MEDIA_ROOT, 'outputs'), exist_ok=True)
            output_filename = f"processed_{os.path.basename(full_temp_path)}"
            output_filepath = os.path.join(settings.MEDIA_ROOT, 'outputs', output_filename)
            cv2.imwrite(output_filepath, img)
            
            # Processed image URL
            processed_image_url = f"{settings.MEDIA_URL}outputs/{output_filename}"
            
            # Clean up raw upload file
            if os.path.exists(full_temp_path):
                os.remove(full_temp_path)
                
            return Response({
                "requestId": str(np.random.randint(100000, 999999)),
                "imageWidth": width,
                "imageHeight": height,
                "processedImage": processed_image_url,
                "detections": detections
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            # Clean up on error
            if os.path.exists(full_temp_path):
                os.remove(full_temp_path)
            return Response({"error": f"Error processing image: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DetectFrameView(APIView):
    def post(self, request):
        if 'frame' not in request.FILES:
            return Response({"error": "No video frame file provided"}, status=status.HTTP_400_BAD_REQUEST)
            
        frame_file = request.FILES['frame']
        
        # Save temporary frame
        temp_path = default_storage.save(f"uploads/frame_{frame_file.name}", frame_file)
        full_temp_path = os.path.join(settings.MEDIA_ROOT, temp_path)
        
        try:
            img = cv2.imread(full_temp_path)
            if img is None:
                return Response({"error": "Failed to read frame file"}, status=status.HTTP_400_BAD_REQUEST)
                
            height, width, _ = img.shape
            yolo = get_yolo_model()
            detections = []
            
            if yolo is not None:
                results = yolo(img)
                for result in results:
                    boxes = result.boxes
                    for box in boxes:
                        cls_id = int(box.cls[0].item())
                        if cls_id in [2, 5, 7]:
                            detect_conf = float(box.conf[0].item())
                            xyxy = box.xyxy[0].cpu().numpy().astype(int)
                            x_min, y_min, x_max, y_max = xyxy
                            
                            w = x_max - x_min
                            h = y_max - y_min
                            pad_x = int(w * 0.1)
                            pad_y = int(h * 0.1)
                            
                            x_min_pad = max(0, x_min - pad_x)
                            y_min_pad = max(0, y_min - pad_y)
                            x_max_pad = min(width, x_max + pad_x)
                            y_max_pad = min(height, y_max + pad_y)
                            
                            crop = img[y_min_pad:y_max_pad, x_min_pad:x_max_pad]
                            manufacturer_label = "Unknown Manufacturer"
                            manufacturer_conf = 0.0
                            is_unknown = True
                            
                            if crop.size > 0:
                                manufacturer_label, manufacturer_conf, is_unknown = classify_cropped_image(crop)
                                
                            detections.append({
                                "objectLabel": "car" if cls_id == 2 else ("bus" if cls_id == 5 else "truck"),
                                "detectionConfidence": round(detect_conf, 4),
                                "box": {
                                    "x": int(x_min),
                                    "y": int(y_min),
                                    "width": int(w),
                                    "height": int(h)
                                },
                                "manufacturerLabel": manufacturer_label,
                                "manufacturerConfidence": manufacturer_conf,
                                "unknownManufacturer": is_unknown
                            })
                            
            # Clean up frame file
            if os.path.exists(full_temp_path):
                os.remove(full_temp_path)
                
            return Response({
                "requestId": str(np.random.randint(100000, 999999)),
                "imageWidth": width,
                "imageHeight": height,
                "processedImage": "", # Blank for frame responses to optimize bandwidth
                "detections": detections
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            if os.path.exists(full_temp_path):
                os.remove(full_temp_path)
            return Response({"error": f"Error processing frame: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
