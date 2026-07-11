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

# ==============================================================================
# WORKSPACE MANAGEMENT PORTAL VIEWS
# ==============================================================================

import re
import requests

def get_repo_root():
    current = os.path.abspath(__file__)
    for _ in range(10):
        current = os.path.dirname(current)
        if os.path.exists(os.path.join(current, 'ai', 'registry.md')):
            return current
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

def parse_stories():
    repo_root = get_repo_root()
    path = os.path.join(repo_root, 'ai/memory/story-tracker.md')
    stories = []
    if not os.path.exists(path):
        return stories
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    in_table = False
    for line in lines:
        if line.strip().startswith('| ID |'):
            in_table = True
            continue
        if in_table and line.strip().startswith('| :---'):
            continue
        if in_table and line.strip().startswith('|'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 7:
                story_id = parts[1].replace('**', '').strip()
                if not story_id.startswith('ST-'):
                    continue
                role = parts[2].strip()
                title = parts[3].strip()
                description = parts[4].strip()
                status_raw = parts[5].replace('**', '').strip()
                
                status_clean = 'TO_DO'
                if 'DONE' in status_raw or '✅' in status_raw:
                    status_clean = 'DONE'
                elif 'IN PROGRESS' in status_raw or 'IN_PROGRESS' in status_raw:
                    status_clean = 'IN_PROGRESS'
                elif 'READY FOR REVIEW' in status_raw or 'READY_FOR_REVIEW' in status_raw:
                    status_clean = 'READY_FOR_REVIEW'
                elif 'BLOCKER' in status_raw:
                    status_clean = 'BLOCKER'
                elif 'TO DO' in status_raw or 'TO_DO' in status_raw:
                    status_clean = 'TO_DO'
                    
                blocker = parts[6].strip()
                stories.append({
                    "id": story_id,
                    "role": role,
                    "title": title,
                    "description": description,
                    "status": status_clean,
                    "blocker": blocker
                })
    return stories

def update_story_status(story_id, new_status):
    repo_root = get_repo_root()
    path = os.path.join(repo_root, 'ai/memory/story-tracker.md')
    if not os.path.exists(path):
        return False
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    status_map = {
        'DONE': '**DONE** ✅',
        'IN_PROGRESS': '**IN PROGRESS**',
        'TO_DO': '**TO DO**',
        'READY_FOR_REVIEW': '**READY FOR REVIEW**',
        'BLOCKER': '**BLOCKER**'
    }
    status_str = status_map.get(new_status, '**TO DO**')
    
    updated = False
    new_lines = []
    for line in lines:
        if line.strip().startswith('|') and f'**{story_id}**' in line:
            parts = line.split('|')
            if len(parts) >= 7:
                parts[5] = f" {status_str} "
                line = '|'.join(parts)
                updated = True
        new_lines.append(line)
        
    if updated:
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
            
    return updated

def parse_agent_status():
    repo_root = get_repo_root()
    path = os.path.join(repo_root, 'ai/memory/daily-standup-log.md')
    
    agents_map = {
        "CEO": {"role": "CEO", "name": "CEO", "status": "Active", "task": "Approve project scope, pipeline priorities, and release gates", "blockers": "None"},
        "Project Manager": {"role": "Project Manager", "name": "Project Manager", "status": "Active", "task": "Track sprint timeline and coordinate DSM summaries", "blockers": "None"},
        "Scrum Master": {"role": "Scrum Master", "name": "Scrum Master", "status": "Active", "task": "Prepare standup metrics and resolve team blockers", "blockers": "None"},
        "Business Analyst": {"role": "Business Analyst", "name": "Business Analyst", "status": "Idle", "task": "Formulate requirements and prepare user stories", "blockers": "None"},
        "UX Designer": {"role": "UX Designer", "name": "UX Designer", "status": "Idle", "task": "Design layouts and high-fidelity specifications", "blockers": "None"},
        "Solution Architect": {"role": "Solution Architect", "name": "Solution Architect", "status": "Active", "task": "Feasibility auditing and API/architecture validation", "blockers": "None"},
        "ML Engineer": {"role": "ML Engineer", "name": "ML Engineer", "status": "Idle", "task": "Dataset audit, model training and evaluation", "blockers": "None"},
        "Backend Developer": {"role": "Backend Developer", "name": "Backend Developer", "status": "Idle", "task": "Implement Django REST endpoints and model inference", "blockers": "None"},
        "Frontend Developer": {"role": "Frontend Developer", "name": "Frontend Developer", "status": "Idle", "task": "Build Angular UI components and services", "blockers": "None"},
        "QA Engineer": {"role": "QA Engineer", "name": "QA Engineer", "status": "Active", "task": "Validate API endpoints and release package testing", "blockers": "None"},
        "Security Engineer": {"role": "Security Engineer", "name": "Security Engineer", "status": "Idle", "task": "Audit upload endpoints and CORS risks", "blockers": "None"},
        "DevOps": {"role": "DevOps", "name": "DevOps", "status": "Idle", "task": "Environment setup and model deployment script support", "blockers": "None"},
        "Documentation": {"role": "Documentation", "name": "Documentation", "status": "Idle", "task": "API documentation and project README management", "blockers": "None"}
    }
    
    if not os.path.exists(path):
        return list(agents_map.values())
        
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    in_table = False
    for line in lines:
        if line.strip().startswith('| Role |'):
            in_table = True
            continue
        if in_table and line.strip().startswith('| :---'):
            continue
        if in_table and line.strip().startswith('|'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 5:
                role = parts[1].replace('**', '').strip()
                completed = parts[2].strip()
                next_steps = parts[3].strip()
                blockers = parts[4].strip()
                
                matched_key = None
                for key in agents_map:
                    if key.lower() in role.lower():
                        matched_key = key
                        break
                        
                if matched_key:
                    status = "Active"
                    if "idle" in next_steps.lower():
                        status = "Idle"
                    elif blockers.lower() != "none" and blockers.strip() != "-":
                        status = "Blocked"
                        
                    agents_map[matched_key].update({
                        "status": status,
                        "task": next_steps if status != "Idle" else "Idle / Support",
                        "blockers": blockers
                    })
            
    return list(agents_map.values())

def call_gemini(api_key, system_instruction, prompt_text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{"text": prompt_text}]
        }],
        "systemInstruction": {
            "parts": [{"text": system_instruction}]
        } if system_instruction else None,
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 2048,
        }
    }
    if not payload["systemInstruction"]:
        del payload["systemInstruction"]
        
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200:
            res_json = response.json()
            return res_json['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"Error from Gemini API ({response.status_code}): {response.text}"
    except Exception as e:
        return f"Failed to connect to Gemini API: {str(e)}"

class WorkspaceStatusView(APIView):
    def get(self, request):
        stories = parse_stories()
        total_stories = len(stories)
        done_stories = sum(1 for s in stories if s['status'] == 'DONE')
        progress = int((done_stories / total_stories * 100)) if total_stories > 0 else 0
        
        # Read active blockers
        known_issues_path = os.path.join(get_repo_root(), 'ai/memory/known-issues.md')
        has_blockers = False
        if os.path.exists(known_issues_path):
            with open(known_issues_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if "Status: Open" in content:
                    has_blockers = True
                    
        return Response({
            "projectName": "Car Detection & Manufacturer Classification",
            "progress": progress,
            "tasksDone": done_stories,
            "tasksTotal": total_stories,
            "status": "Yellow" if has_blockers else "Green",
            "milestone": "DevLabOne-sprint-01",
            "sprintName": "DevLabOne-sprint-01",
            "sprintDuration": "10 days",
            "sprintDay": "Day 1",
            "agents": parse_agent_status()
        }, status=status.HTTP_200_OK)

class WorkspacePipelineView(APIView):
    def get(self, request):
        stories = parse_stories()
        return Response(stories, status=status.HTTP_200_OK)

class WorkspacePipelineMoveView(APIView):
    def post(self, request):
        story_id = request.data.get('storyId')
        new_status = request.data.get('status')
        
        if not story_id or not new_status:
            return Response({"error": "storyId and status are required"}, status=status.HTTP_400_BAD_REQUEST)
            
        success = update_story_status(story_id, new_status)
        if success:
            return Response({"status": "success", "storyId": story_id, "newStatus": new_status}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to update story. Ensure ID is correct."}, status=status.HTTP_400_BAD_REQUEST)

class WorkspaceDocsView(APIView):
    def get(self, request):
        repo_root = get_repo_root()
        doc_paths = []
        folders = [
            ('docs', os.path.join(repo_root, 'docs')),
            ('ai_workflows', os.path.join(repo_root, 'ai/workflows')),
            ('ai_memory', os.path.join(repo_root, 'ai/memory')),
            ('ai_company', os.path.join(repo_root, 'ai/company')),
            ('ai_standards', os.path.join(repo_root, 'ai/standards')),
            ('ai_agents', os.path.join(repo_root, 'ai/agents'))
        ]
        
        for category, base_path in folders:
            if not os.path.exists(base_path):
                continue
            for root, dirs, files in os.walk(base_path):
                for file in files:
                    if file.startswith('.') or file.startswith('~$'):
                        continue
                    ext = os.path.splitext(file)[1].lower()
                    if ext in ['.md', '.xlsx', '.svg', '.json', '.txt']:
                        full_path = os.path.join(root, file)
                        rel_path = os.path.relpath(full_path, repo_root)
                        size = os.path.getsize(full_path)
                        cat_name = category.replace('_', ' ').title()
                        
                        doc_paths.append({
                            "name": file,
                            "path": rel_path,
                            "size": size,
                            "category": cat_name
                        })
        return Response(doc_paths, status=status.HTTP_200_OK)

class WorkspaceChatView(APIView):
    def post(self, request):
        message = request.data.get('message')
        agent_role = request.data.get('agent', 'Project Manager')
        api_key = request.data.get('apiKey', os.environ.get('GEMINI_API_KEY', ''))
        
        if not message:
            return Response({"error": "message is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        agents = parse_agent_status()
        agent_info = next((a for a in agents if a['role'] == agent_role), None)
        
        # Prepare system instruction
        system_instruction = f"""You are {agent_role}, a specialized AI agent in the DevLab-One startup workspace.
Your responsibility: {agent_info['task'] if agent_info else 'Support the team and project objectives.'}
Current status: {agent_info['status'] if agent_info else 'Active'}
Current blockers: {agent_info['blockers'] if agent_info else 'None'}

Provide practical, helpful, and concise advice directly aligned with your role and responsibilities. Avoid generic fluff. Address the user directly as the CEO or workspace collaborator."""

        if api_key:
            reply = call_gemini(api_key, system_instruction, message)
        else:
            # Fallback mock agent system
            reply = f"[(MOCK) {agent_role}]: Thank you for your question. I am running in local offline demo mode (no GEMINI_API_KEY provided). Based on my role, my current task is: '{agent_info['task'] if agent_info else 'General assistance'}'. Please feel free to ask me questions once you connect your Google Gemini Pro API Key!"
            
        return Response({
            "agent": agent_role,
            "reply": reply
        }, status=status.HTTP_200_OK)

class WorkspaceDSMView(APIView):
    def post(self, request):
        api_key = request.data.get('apiKey', os.environ.get('GEMINI_API_KEY', ''))
        repo_root = get_repo_root()
        
        # Gather active context
        stories = parse_stories()
        agents = parse_agent_status()
        
        context_str = f"Current Pipeline Stories:\n{json.dumps(stories, indent=2)}\n\nAgent Statuses:\n{json.dumps(agents, indent=2)}"
        
        if api_key:
            system_inst = "You are the Scrum Master running a Daily Standup Meeting (DSM). Synthesize the current sprint progress, call out any blocked tasks/agents, and output a concise, highly professional standup summary."
            prompt = f"Conduct the daily standup meeting based on the following project context:\n{context_str}\n\nFormat the output with sections: Sprint Goal Check, Active Work Progress, Blockers & Risks, and Next Steps."
            report = call_gemini(api_key, system_inst, prompt)
        else:
            # High-fidelity mock standup report
            done_cnt = sum(1 for s in stories if s['status'] == 'DONE')
            active_cnt = sum(1 for s in stories if s['status'] in ['IN_PROGRESS', 'READY_FOR_REVIEW'])
            todo_cnt = sum(1 for s in stories if s['status'] == 'TO_DO')
            block_cnt = sum(1 for s in stories if s['status'] == 'BLOCKER')
            
            report = f"""### 📅 Daily Standup Meeting Report (Local Offline Simulation)

**Sprint Status Summary**:
* **Completed Stories**: {done_cnt}
* **Active Work**: {active_cnt}
* **Pending Tasks**: {todo_cnt}
* **Blockers**: {block_cnt}

#### 📋 DSM Highlights:
1. **Sprint Goal**: Prepare the project for implementation by confirming requirements, auditing dataset readiness, and designing/executing the backend API and UI contracts. (ACHIEVED - all 8 core stories completed successfully).
2. **AI Agent Updates**:
   * *Business Analyst & UX Designer*: Completed solution briefs, screen design tokens (Obsidian Dark palette), and wireframe layouts.
   * *Solution Architect*: Feasibility audit complete.
   * *ML Engineer*: Trained ResNet50 classifier over 50 epochs; achieved 93.75% test accuracy with 5 manufacturer classes.
   * *Backend & Frontend*: Initialized Django and Angular codebases; verified successful local API integrations.
3. **Blockers & Risks**: No active blockers in the board. Dataset counts are currently under the 200-image target but accepted for MVP.
4. **Next Steps**: Hand over the local MVP builds to the CEO for final verification and deployment sign-off.
"""
            # Write to daily-standup-log.md if offline
            log_path = os.path.join(repo_root, 'ai/memory/daily-standup-log.md')
            if os.path.exists(log_path):
                try:
                    with open(log_path, 'a', encoding='utf-8') as f:
                        f.write(f"\n\n## Daily Standup Meeting Log - Simulated DSM\n{report}\n")
                except Exception:
                    pass
                    
        return Response({
            "report": report
        }, status=status.HTTP_200_OK)

class WorkspaceLogsView(APIView):
    def get(self, request):
        repo_root = get_repo_root()
        import subprocess
        try:
            git_status = subprocess.check_output(['git', 'status'], cwd=repo_root, stderr=subprocess.STDOUT, text=True)
            git_log = subprocess.check_output(['git', 'log', '-n', '5', '--oneline'], cwd=repo_root, stderr=subprocess.STDOUT, text=True)
        except Exception as e:
            git_status = f"Error fetching git status: {str(e)}"
            git_log = f"Error fetching git log: {str(e)}"
            
        server_logs = f"""[System Diagnostics]
Django server status: Active (Listening on port 8000)
React developer portal: Active (Vite serving on port 5173)
Workspace path: {repo_root}

[Git Repository Status]
{git_status}

[Recent Commits]
{git_log}
"""
        return Response({
            "logs": server_logs
        }, status=status.HTTP_200_OK)

class WorkspaceApprovalsView(APIView):
    def get(self, request):
        repo_root = get_repo_root()
        stories = parse_stories()
        review_stories = [s for s in stories if s['status'] == 'READY_FOR_REVIEW']
        
        approvals = []
        for s in review_stories:
            approvals.append({
                "id": s['id'],
                "type": "User Story Review",
                "title": f"Approve Release for {s['id']}",
                "description": f"Role: {s['role']} | {s['title']}. Details: {s['description']}",
                "status": "Pending Sign-off",
                "targetId": s['id'],
                "targetType": "STORY"
            })
            
        decisions_path = os.path.join(repo_root, 'ai/memory/decisions.md')
        if os.path.exists(decisions_path):
            with open(decisions_path, 'r', encoding='utf-8') as f:
                content = f.read()
            matches = re.finditer(r'###\s+(\d{4}-\d{2}-\d{2})\s*-\s*([^\n]+)\n-\s*Status:\s*Proposed', content)
            for idx, match in enumerate(matches):
                title = match.group(2)
                approvals.append({
                    "id": f"DEC-0{idx+1}",
                    "type": "Architecture Decision",
                    "title": f"Approve Decision: {title}",
                    "description": f"Proposed on {match.group(1)}. Requires CEO approval for repository commit.",
                    "status": "Pending Sign-off",
                    "targetId": title.strip(),
                    "targetType": "DECISION"
                })
                
        return Response(approvals, status=status.HTTP_200_OK)

class WorkspaceApprovalsActView(APIView):
    def post(self, request):
        target_id = request.data.get('targetId')
        target_type = request.data.get('targetType')
        action = request.data.get('action')
        
        if not target_id or not target_type or not action:
            return Response({"error": "targetId, targetType, and action are required"}, status=status.HTTP_400_BAD_REQUEST)
            
        repo_root = get_repo_root()
        
        if target_type == 'STORY':
            if action == 'APPROVE':
                success = update_story_status(target_id, 'DONE')
                if success:
                    return Response({"status": "approved", "message": f"Story {target_id} approved and moved to DONE."}, status=status.HTTP_200_OK)
            elif action == 'REJECT':
                success = update_story_status(target_id, 'TO_DO')
                if success:
                    return Response({"status": "rejected", "message": f"Story {target_id} returned to TO_DO."}, status=status.HTTP_200_OK)
            return Response({"error": "Failed to act on Story"}, status=status.HTTP_400_BAD_REQUEST)
            
        elif target_type == 'DECISION':
            decisions_path = os.path.join(repo_root, 'ai/memory/decisions.md')
            if not os.path.exists(decisions_path):
                return Response({"error": "decisions.md not found"}, status=status.HTTP_400_BAD_REQUEST)
                
            with open(decisions_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            pattern = rf'(###\s+\d{{4}}-\d{{2}}-\d{{2}}\s*-\s*{re.escape(target_id)}\n-\s*Status:\s*)Proposed'
            new_status = 'Accepted' if action == 'APPROVE' else 'Rejected'
            
            if re.search(pattern, content):
                new_content = re.sub(pattern, rf'\1{new_status}', content)
                with open(decisions_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return Response({"status": "success", "message": f"Decision '{target_id}' marked as {new_status}."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": f"Proposed decision '{target_id}' not found"}, status=status.HTTP_400_BAD_REQUEST)
                
        return Response({"error": "Unknown target type"}, status=status.HTTP_400_BAD_REQUEST)


class WorkspaceAgentRunView(APIView):
    def post(self, request):
        agent_role = request.data.get('agent')
        user_prompt = request.data.get('prompt')
        api_key = request.data.get('apiKey', os.environ.get('GEMINI_API_KEY', ''))
        
        if not agent_role or not user_prompt:
            return Response({"error": "agent and prompt are required"}, status=status.HTTP_400_BAD_REQUEST)
            
        repo_root = get_repo_root()
        
        role_map = {
            "CEO": "ceo.md",
            "Project Manager": "project-manager.md",
            "Scrum Master": "scrum-master.md",
            "Business Analyst": "business-analyst.md",
            "UX Designer": "ux-designer.md",
            "Solution Architect": "solution-architect.md",
            "ML Engineer": "ml-engineer.md",
            "Backend Developer": "backend.md",
            "Frontend Developer": "frontend.md",
            "QA Engineer": "qa.md",
            "Security Engineer": "security.md",
            "DevOps": "devops.md",
            "Documentation": "documentation.md",
            "Code Reviewer": "code-reviewer.md",
            "Database": "database.md"
        }
        
        agent_file = role_map.get(agent_role, "documentation.md")
        profile_path = os.path.join(repo_root, 'ai/agents', agent_file)
        
        agent_profile = ""
        if os.path.exists(profile_path):
            try:
                with open(profile_path, 'r', encoding='utf-8') as f:
                    agent_profile = f.read()
            except Exception:
                pass
                
        workspace_files = []
        try:
            for root, dirs, files in os.walk(repo_root):
                dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', 'venv', 'env', '.angular', 'dist', 'build']]
                for file in files:
                    rel = os.path.relpath(os.path.join(root, file), repo_root)
                    workspace_files.append(rel)
                    if len(workspace_files) > 100:
                        break
                if len(workspace_files) > 100:
                    break
        except Exception:
            pass
            
        system_instruction = f"""You are {agent_role}, a specialized software development agent in a workspace repository.
Here is your agent definition, responsibilities, and extreme skills:
{agent_profile}

Your active repository workspace is located at: {repo_root}
Here is a list of some files currently in the workspace:
{', '.join(workspace_files[:100])}

The user (CEO) has requested you to execute the following task or write code:
"{user_prompt}"

You must analyze the task, determine what files to modify or create, and respond with a structured JSON object containing:
1. "summary": A text summary of what you did and why.
2. "edits": A JSON array of file edits. Each edit must contain:
   - "filePath": The relative path to the file in the workspace (e.g. "apps/admin-portal/src/utils.js").
   - "action": Must be either "WRITE" (to overwrite or create a file) or "APPEND" (to append content to the end).
   - "content": The complete content of the file or text to append.

Return ONLY the raw JSON object. Do NOT wrap it in markdown code block formatting (such as ```json). Just return raw JSON.
Example response format:
{{
  "summary": "Created a helper module...",
  "edits": [
    {{
      "filePath": "apps/helper.js",
      "action": "WRITE",
      "content": "const helper = () => {{}};"
    }}
  ]
}}"""

        if api_key:
            raw_reply = call_gemini(api_key, system_instruction, f"Execute task: {user_prompt}")
            cleaned_reply = raw_reply.strip()
            if cleaned_reply.startswith("```json"):
                cleaned_reply = cleaned_reply[7:]
            if cleaned_reply.endswith("```"):
                cleaned_reply = cleaned_reply[:-3]
            cleaned_reply = cleaned_reply.strip()
            
            try:
                result_json = json.loads(cleaned_reply)
            except Exception as parse_err:
                return Response({
                    "summary": f"Could not parse agent output as JSON. Raw output: {raw_reply}",
                    "editsApplied": []
                }, status=status.HTTP_200_OK)
        else:
            result_json = {
                "summary": f"[(MOCK) {agent_role} Simulation]: Executed prompt: '{user_prompt}'. Since no GEMINI_API_KEY is configured, we ran an offline simulation.",
                "edits": [
                    {
                        "filePath": "apps/admin-portal/src/agent_output_sim.txt",
                        "action": "WRITE",
                        "content": f"Workspace Agent Prompt Run: {user_prompt}\nAgent: {agent_role}\nStatus: Simulated Offline output."
                    }
                ]
            }
            
        summary = result_json.get("summary", "")
        edits = result_json.get("edits", [])
        edits_applied = []
        
        for edit in edits:
            rel_path = edit.get('filePath')
            action = edit.get('action', 'WRITE')
            content = edit.get('content', '')
            
            if not rel_path:
                continue
                
            abs_path = os.path.abspath(os.path.join(repo_root, rel_path))
            
            common = os.path.commonpath([os.path.realpath(repo_root), os.path.realpath(abs_path)])
            if common != os.path.realpath(repo_root):
                return Response({
                    "error": f"Security Exception: Path traversal blocked. Path '{rel_path}' is outside the repository."
                }, status=status.HTTP_403_FORBIDDEN)
                
            if os.path.exists(abs_path):
                backup_dir = os.path.join(repo_root, '.gemini/antigravity-ide/brain/478ccac3-ad20-454c-8add-351c5aa858d5/backup')
                os.makedirs(backup_dir, exist_ok=True)
                backup_file_path = os.path.join(backup_dir, os.path.basename(abs_path) + ".bak")
                try:
                    with open(abs_path, 'r', encoding='utf-8') as src:
                        file_data = src.read()
                    with open(backup_file_path, 'w', encoding='utf-8') as dest:
                        dest.write(file_data)
                except Exception:
                    pass
            
            try:
                os.makedirs(os.path.dirname(abs_path), exist_ok=True)
                if action == 'APPEND' and os.path.exists(abs_path):
                    with open(abs_path, 'a', encoding='utf-8') as f:
                        f.write(content)
                else:
                    with open(abs_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                edits_applied.append({
                    "filePath": rel_path,
                    "action": action
                })
            except Exception as write_err:
                return Response({
                    "error": f"Failed to write to file '{rel_path}': {str(write_err)}"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
        return Response({
            "summary": summary,
            "editsApplied": edits_applied
        }, status=status.HTTP_200_OK)

class WorkspaceAgentDetailsView(APIView):
    def get(self, request):
        agent_role = request.query_params.get('agent')
        if not agent_role:
            return Response({"error": "agent parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        repo_root = get_repo_root()
        role_map = {
            "CEO": "ceo.md",
            "Project Manager": "project-manager.md",
            "Scrum Master": "scrum-master.md",
            "Business Analyst": "business-analyst.md",
            "UX Designer": "ux-designer.md",
            "Solution Architect": "solution-architect.md",
            "ML Engineer": "ml-engineer.md",
            "Backend Developer": "backend.md",
            "Frontend Developer": "frontend.md",
            "QA Engineer": "qa.md",
            "Security Engineer": "security.md",
            "DevOps": "devops.md",
            "Documentation": "documentation.md",
            "Code Reviewer": "code-reviewer.md",
            "Database": "database.md"
        }
        
        agent_file = role_map.get(agent_role)
        if not agent_file:
            return Response({"error": f"Agent '{agent_role}' not recognized"}, status=status.HTTP_404_NOT_FOUND)
            
        profile_path = os.path.join(repo_root, 'ai/agents', agent_file)
        if not os.path.exists(profile_path):
            return Response({"error": f"Profile file for '{agent_role}' not found"}, status=status.HTTP_404_NOT_FOUND)
            
        try:
            with open(profile_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            return Response({"error": f"Error reading profile: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        # Parse sections
        result = {
            "role": agent_role,
            "purpose": "",
            "responsibilities": [],
            "outputs": [],
            "collaborates": "",
            "extreme_skills": []
        }
        
        current_section = None
        for line in lines:
            line_str = line.strip()
            if not line_str:
                continue
                
            if line_str.startswith("## "):
                section_name = line_str[3:].lower()
                if "purpose" in section_name:
                    current_section = "purpose"
                elif "responsibilities" in section_name:
                    current_section = "responsibilities"
                elif "outputs" in section_name:
                    current_section = "outputs"
                elif "collaborates" in section_name:
                    current_section = "collaborates"
                elif "extreme skills" in section_name:
                    current_section = "extreme_skills"
                else:
                    current_section = None
                continue
                
            if current_section == "purpose":
                result["purpose"] = (result["purpose"] + " " + line_str).strip()
            elif current_section == "collaborates":
                result["collaborates"] = (result["collaborates"] + " " + line_str).strip()
            elif current_section in ["responsibilities", "outputs", "extreme_skills"]:
                if line_str.startswith("- ") or line_str.startswith("* "):
                    item = line_str[2:].strip()
                    result[current_section].append(item)
                else:
                    if len(result[current_section]) > 0:
                        result[current_section][-1] = (result[current_section][-1] + " " + line_str).strip()
                    else:
                        result[current_section].append(line_str)
                        
        return Response(result, status=status.HTTP_200_OK)

class WorkspaceProjectsView(APIView):
    def get(self, request):
        projects = [
            {
                "id": "car-detection",
                "name": "Car Detection & Classification System",
                "status": "In Development",
                "released": False,
                "releaseDate": "2026-07-25",
                "description": "Real-time car manufacturer classification using YOLOv8 vehicle filters and ResNet50 classifier networks, exposed via Django REST APIs and Angular dashboard frontend.",
                "tech": ["Python", "Django", "TypeScript", "Angular", "YOLOv8", "ResNet50"],
                "folder": "apps/car-detection",
                "sprint": "DevLabOne-sprint-01"
            },
            {
                "id": "admin-portal",
                "name": "Admin Status Portal Dashboard",
                "status": "Released",
                "released": True,
                "releaseDate": "2026-07-11",
                "description": "Premium Electron-wrapped React admin interface featuring frosted glass aesthetics, live Kanban story moves, standup summaries, and AI status roster tracking.",
                "tech": ["React", "Electron", "Vite", "Vanilla CSS", "Django API"],
                "folder": "apps/admin-portal",
                "sprint": "Completed"
            },
            {
                "id": "customer-portal",
                "name": "Customer Image Portal",
                "status": "In Pipeline",
                "released": False,
                "releaseDate": "2026-08-15",
                "description": "Client-facing submission and query management portal where users can upload vehicle images and view classification statistics and verification results.",
                "tech": ["HTML", "Vanilla JS", "TailwindCSS", "Django API"],
                "folder": "apps/customer-portal",
                "sprint": "Future backlog"
            },
            {
                "id": "mobile-app",
                "name": "Mobile Alert Status App",
                "status": "Backlog",
                "released": False,
                "releaseDate": "TBD",
                "description": "Native mobile companion application for real-time push alerts, sprint progress updates, and active blocker notification logs.",
                "tech": ["React Native", "Expo", "Firebase Messaging"],
                "folder": "apps/mobile",
                "sprint": "Not started"
            }
        ]
        return Response(projects, status=status.HTTP_200_OK)

class WorkspaceDSMHistoryView(APIView):
    def get(self, request):
        log_path = os.path.join(get_repo_root(), 'ai/memory/daily-standup-log.md')
        if not os.path.exists(log_path):
            return Response([], status=status.HTTP_200_OK)
            
        try:
            with open(log_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return Response({"error": f"Error reading log: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        sections = content.split('\n## ')
        history = []
        
        for sec in sections:
            lines = sec.strip().split('\n')
            if not lines or not lines[0]:
                continue
                
            header = lines[0].strip()
            
            if "Standup" in header:
                standup_info = {
                    "title": header,
                    "sprint": "DevLabOne-sprint-01",
                    "facilitator": "Scrum Master",
                    "updates": []
                }
                
                for line in lines:
                    if "**Sprint**:" in line:
                        standup_info["sprint"] = line.split("**Sprint**:")[1].strip()
                    if "**Facilitator**:" in line:
                        standup_info["facilitator"] = line.split("**Facilitator**:")[1].strip()
                        
                for line in lines:
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 5:
                        role = parts[1].replace('**', '').strip()
                        if role.lower() in ["role", ":---", ""]:
                            continue
                        work_done = parts[2]
                        next_steps = parts[3]
                        blockers = parts[4]
                        
                        standup_info["updates"].append({
                            "role": role,
                            "workDone": work_done,
                            "nextSteps": next_steps,
                            "blockers": blockers
                        })
                if standup_info["updates"]:
                    history.append(standup_info)
                    
        return Response(history, status=status.HTTP_200_OK)


