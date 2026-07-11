import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CarDetectionService, Detection, ModelInfo } from '../services/car-detection.service';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css'
})
export class Dashboard {
  private apiService = inject(CarDetectionService);

  // States
  protected modelInfo = signal<ModelInfo | null>(null);
  protected isProcessing = signal<boolean>(false);
  protected processedImageUrl = signal<string | null>(null);
  protected detections = signal<Detection[]>([]);
  protected uploadError = signal<string | null>(null);
  protected activeHoverIdx = signal<number | null>(null);

  constructor() {
    this.fetchModelInfo();
  }

  fetchModelInfo() {
    this.apiService.getModelInfo().subscribe({
      next: (info) => this.modelInfo.set(info),
      error: () => console.log('Error fetching model info. Backend might be offline.')
    });
  }

  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      this.processImage(input.files[0]);
    }
  }

  onDragOver(event: DragEvent) {
    event.preventDefault();
  }

  onDrop(event: DragEvent) {
    event.preventDefault();
    if (event.dataTransfer && event.dataTransfer.files && event.dataTransfer.files[0]) {
      this.processImage(event.dataTransfer.files[0]);
    }
  }

  processImage(file: File) {
    // Validate size (max 10MB)
    if (file.size > 10 * 1024 * 1024) {
      this.uploadError.set('File size exceeds the 10MB limit.');
      return;
    }

    this.isProcessing.set(true);
    this.uploadError.set(null);
    this.processedImageUrl.set(null);
    this.detections.set([]);

    this.apiService.detectImage(file).subscribe({
      next: (res) => {
        // Build base URL for processed image
        const imgUrl = res.processedImage ? `http://localhost:8000${res.processedImage}` : null;
        this.processedImageUrl.set(imgUrl);
        this.detections.set(res.detections);
        this.isProcessing.set(false);
      },
      error: (err) => {
        this.uploadError.set(err?.error?.error || 'Failed to process image. Make sure Django backend is running.');
        this.isProcessing.set(false);
      }
    });
  }

  setHover(index: number | null) {
    this.activeHoverIdx.set(index);
  }
}
