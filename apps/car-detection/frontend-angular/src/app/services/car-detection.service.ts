import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface DetectionBox {
  x: number;
  y: number;
  width: number;
  height: number;
}

export interface Detection {
  objectLabel: string;
  detectionConfidence: number;
  box: DetectionBox;
  manufacturerLabel: string;
  manufacturerConfidence: number;
  unknownManufacturer: boolean;
}

export interface DetectionResponse {
  requestId: string;
  imageWidth: number;
  imageHeight: number;
  processedImage: string;
  detections: Detection[];
}

export interface ModelInfo {
  detector: string;
  classifier: string;
  manufacturers: string[];
  unknownThreshold: number;
  selectedEpoch: number;
  modelVersion: string;
}

@Injectable({
  providedIn: 'root'
})
export class CarDetectionService {
  private http = inject(HttpClient);
  private baseUrl = 'http://localhost:8000/api';

  getHealth(): Observable<{ status: string }> {
    return this.http.get<{ status: string }>(`${this.baseUrl}/health/`);
  }

  getModelInfo(): Observable<ModelInfo> {
    return this.http.get<ModelInfo>(`${this.baseUrl}/model/info/`);
  }

  detectImage(imageFile: File): Observable<DetectionResponse> {
    const formData = new FormData();
    formData.append('image', imageFile);
    return this.http.post<DetectionResponse>(`${this.baseUrl}/detect/image/`, formData);
  }

  detectFrame(frameBlob: Blob): Observable<DetectionResponse> {
    const formData = new FormData();
    formData.append('frame', frameBlob, 'frame.jpg');
    return this.http.post<DetectionResponse>(`${this.baseUrl}/detect/frame/`, formData);
  }
}
