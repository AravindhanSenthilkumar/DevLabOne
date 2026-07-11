# DevLab-One Car Detection UX Screen Mockups

This document details the high-fidelity UI design mockups for the two main application screens: **Upload Dashboard** and **Live CCTV Monitor**. The design assets are packaged as fully editable vector layers importable directly into Figma.

---

## 🎨 Figma High-Fidelity UI Design File

The vector design sheets are located at:
*   **Vector UI Layout Design**: [ux_ui_design.svg](file:///Users/aravindhansenthilkumar/Documents/DevLab-One/docs/ux_ui_design.svg)

> [!TIP]
> **Figma Integration**: To open this in Figma, simply drag and drop the `ux_ui_design.svg` file directly onto your Figma workspace canvas. Figma will automatically convert the SVG paths, text nodes, colors, and gradients into fully editable, layered vector frames and shapes.

---

## 💎 Design Tokens & Aesthetics Specifications

Our design uses a custom aesthetic called **Obsidian Glassmorphic Dark Mode**, structured around the following rules:

### 1. Color Palette (Tailored HSL & Sleek Gradients)
-   **Canvas Base Background**: `#090D16` to `#020617` (Deep slate gradient)
-   **Primary Brand Color (Indigo)**: `#6366F1` to `#4F46E5` (Active buttons, borders, and brand assets)
-   **Success Accent (Emerald)**: `#10B981` (High-confidence bounding boxes, active badges, and successful logs)
-   **Warning/Fallback Accent (Amber)**: `#F59E0B` (Low-confidence predictions, untested classes, warning tags)
-   **Danger/Alert Accent (Red)**: `#EF4444` (Stop stream buttons, offline indicators, error logs)
-   **Text/Labels**: `#FFFFFF` (Primary titles), `#E2E8F0` (Card labels), `#94A3B8` (Descriptions), `#4B5563` (Console timestamps)

### 2. Glassmorphic Surface Cards (`url(#glass-card)`)
-   **Background Fill**: `rgba(30, 41, 59, 0.5)` blending into `rgba(15, 23, 42, 0.3)`
-   **Backdrop Filter**: `blur(16px)` to overlay cleanly above running streams or base canvas
-   **Card Border**: `1px solid rgba(255, 255, 255, 0.08)` to reflect light softly along the edges

### 3. Glow Filters (`url(#glow-indigo)` and `url(#glow-green)`)
-   Active vector components (like camera streams, bounding boxes, and active buttons) employ a subtle outer blur shadow with 30% opacity to create a futuristic glowing appearance.

---

## 📺 Detailed Interface Layouts

### Interface Screen 1: Upload Dashboard
-   **Model Stats Header**: Renders live stats displaying detector version, classifier model state, and active training epoch counters.
-   **Manual Dropzone**: Dashed Indigo border surrounding file drop hooks, prompting users to upload photos up to 10MB.
-   **Visual Image Viewport**: Displays processed results. Annotates cars with colored bounding box frames (e.g. green bounding box labeled `AUDI (98.4%)`).
-   **Detections Sidebar**: A stack of glass cards detailing each vehicle's localization confidence and brand classification probability.

### Interface Screen 2: Live CCTV Monitor
-   **Stream Control Bar**: Features a prominent red action button to toggle camera activation status. Includes real-time indicators for frame processing rate (FPS) and API latency metrics.
-   **Video Viewport**: Displays the live video feed. Outlines moving vehicle crops with canvas bounding box overlays.
-   **Retro Logs Console**: A monospace command-line terminal displaying rolling timestamps, backend status reports, model loads, and warning details in retro green formatting.
