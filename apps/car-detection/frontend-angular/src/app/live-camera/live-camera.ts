import { Component, ElementRef, ViewChild, inject, signal, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CarDetectionService, Detection } from '../services/car-detection.service';

interface LogMessage {
  timestamp: string;
  message: string;
  isUnknown: boolean;
}

@Component({
  selector: 'app-live-camera',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './live-camera.html',
  styleUrl: './live-camera.css'
})
export class LiveCamera implements OnDestroy {
  private apiService = inject(CarDetectionService);

  @ViewChild('videoElement') videoElement!: ElementRef<HTMLVideoElement>;
  @ViewChild('overlayCanvas') overlayCanvas!: ElementRef<HTMLCanvasElement>;

  // States
  protected isMonitoring = signal<boolean>(false);
  protected fps = signal<number>(0);
  protected latency = signal<number>(0);
  protected logMessages = signal<LogMessage[]>([]);
  protected cameraError = signal<string | null>(null);

  private mediaStream: MediaStream | null = null;
  private animationFrameId: number | null = null;
  private isProcessingFrame = false;
  private lastFrameTime = 0;
  private frameCount = 0;
  private fpsTimer = 0;

  startMonitoring() {
    this.cameraError.set(null);
    navigator.mediaDevices.getUserMedia({ video: { width: 1280, height: 720 } })
      .then((stream) => {
        this.mediaStream = stream;
        this.videoElement.nativeElement.srcObject = stream;
        this.isMonitoring.set(true);
        this.logMessage('Camera stream initialized. Monitoring started.');
        
        // Start processing loop
        this.lastFrameTime = performance.now();
        this.fpsTimer = performance.now();
        this.frameCount = 0;
        this.animationFrameId = requestAnimationFrame(() => this.processLoop());
      })
      .catch((err) => {
        console.error(err);
        this.cameraError.set('Could not access camera. Ensure permissions are granted.');
      });
  }

  stopMonitoring() {
    this.isMonitoring.set(false);
    if (this.mediaStream) {
      this.mediaStream.getTracks().forEach(track => track.stop());
      this.mediaStream = null;
    }
    if (this.animationFrameId) {
      cancelAnimationFrame(this.animationFrameId);
      this.animationFrameId = null;
    }
    // Clear canvas
    const canvas = this.overlayCanvas.nativeElement;
    const ctx = canvas.getContext('2d');
    ctx?.clearRect(0, 0, canvas.width, canvas.height);
    this.logMessage('Monitoring stopped.');
  }

  private processLoop() {
    if (!this.isMonitoring()) return;

    const now = performance.now();
    
    // FPS tracking
    this.frameCount++;
    if (now - this.fpsTimer >= 1000) {
      this.fps.set(this.frameCount);
      this.frameCount = 0;
      this.fpsTimer = now;
    }

    // Throttled frame capture: process a frame every 500ms
    if (!this.isProcessingFrame && (now - this.lastFrameTime >= 500)) {
      this.captureAndProcessFrame();
      this.lastFrameTime = now;
    }

    this.animationFrameId = requestAnimationFrame(() => this.processLoop());
  }

  private captureAndProcessFrame() {
    const video = this.videoElement.nativeElement;
    const canvas = this.overlayCanvas.nativeElement;
    
    if (video.readyState !== video.HAVE_ENOUGH_DATA) return;

    // Set canvas dimensions to match display dimensions
    const rect = video.getBoundingClientRect();
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.style.width = `${rect.width}px`;
    canvas.style.height = `${rect.height}px`;

    // Draw video frame to an off-screen canvas to extract blob
    const offscreen = document.createElement('canvas');
    offscreen.width = video.videoWidth;
    offscreen.height = video.videoHeight;
    const ctx = offscreen.getContext('2d');
    if (!ctx) return;
    ctx.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

    this.isProcessingFrame = true;
    const sendTime = performance.now();

    offscreen.toBlob((blob) => {
      if (blob) {
        this.apiService.detectFrame(blob).subscribe({
          next: (res) => {
            this.latency.set(Math.round(performance.now() - sendTime));
            this.drawOverlays(res.detections);
            this.isProcessingFrame = false;
          },
          error: () => {
            this.isProcessingFrame = false;
          }
        });
      } else {
        this.isProcessingFrame = false;
      }
    }, 'image/jpeg', 0.85);
  }

  private drawOverlays(detections: Detection[]) {
    const canvas = this.overlayCanvas.nativeElement;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    detections.forEach(det => {
      const { x, y, width, height } = det.box;
      const isUnknown = det.unknownManufacturer;
      const color = isUnknown ? '#f59e0b' : '#10b981'; // Amber vs Emerald

      // Draw bounding box
      ctx.strokeStyle = color;
      ctx.lineWidth = 4;
      ctx.strokeRect(x, y, width, height);

      // Draw label background
      ctx.fillStyle = color;
      const labelText = isUnknown 
        ? `Unknown (${(det.manufacturerConfidence * 100).toFixed(0)}%)` 
        : `${det.manufacturerLabel} (${(det.manufacturerConfidence * 100).toFixed(0)}%)`;
      ctx.font = 'bold 16px Inter, sans-serif';
      const labelWidth = ctx.measureText(labelText).width;
      ctx.fillRect(x, y - 28 >= 0 ? y - 28 : y, labelWidth + 16, 28);

      // Draw label text
      ctx.fillStyle = '#ffffff';
      ctx.fillText(labelText, x + 8, y - 28 >= 0 ? y - 8 : y + 20);

      // Log to Scrolling Terminal if it's a new detection log
      this.logMessage(`Detected: ${det.manufacturerLabel} (Conf: ${(det.manufacturerConfidence*100).toFixed(0)}%)`, isUnknown);
    });
  }

  private logMessage(text: string, isUnknown = false) {
    const timestamp = new Date().toLocaleTimeString();
    const updatedLogs = [
      { timestamp, message: text, isUnknown },
      ...this.logMessages().slice(0, 49) // Keep last 50 entries
    ];
    this.logMessages.set(updatedLogs);
  }

  ngOnDestroy() {
    this.stopMonitoring();
  }
}
