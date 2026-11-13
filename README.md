# A Robust Multi-Task Vision Transformer Framework for Image Forgery Localization, Detection, and Classification 🔬
### 23CSE498 – Project Phase II (External Review) • Team Number: 39

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

Interactive cyber-forensic web evaluation portal developed by **Team 39 (Amrita Vishwa Vidyapeetham)** for the research project:
**A Robust Multi-Task Vision Transformer Framework for Image Forgery Localization, Detection, and Classification**.

It pairs self-supervised Vision Transformer (DINOv3 ViT-S/14 + LoRA) representations with a specialized **Copy-Move Self-Correlation Branch** (48 px Chebyshev exclusion) and a multi-stage convolutional mask decoder to achieve high-resolution, end-to-end image tampering detection, pixel localization, and multi-label forgery categorization.

---

## 🌟 Key Capabilities

- **Dual-View Integrated Portal**: Seamlessly switch between the **Interactive Forensic Lab (Live Demo)** and the **Project Showcase & Documentation Portal** (Objectives, Problem Statement, Methodology, Team Details, Progress, Specs, Repos, Demonstration).
- **Interactive Split Wipe Viewer**: Real-time sliding curtain wipe comparing the pristine original image with the pixel-level anomaly heatmap overlay.
- **Multiple Visualization Modes**:
  - *Curtain Split*: Dual-layered draggable split line with real-time percentage tracking.
  - *Side-by-Side*: Direct side-by-side comparative inspection.
  - *Heatmap Overlay*: Pure anomaly localization heatmap with variable alpha opacity blending.
  - *Bounding Box*: Automated contour boundary detection highlighting suspicious regions.
- **Hierarchical Diagnostic Stages**:
  - **Stage 1 (DetectionHead)**: Binary classification (Authentic vs. Tampered) with confidence score and decision margin telemetry.
  - **Stage 2 (TypeHead)**: Multi-label classification breakdown (*Copy-Move*, *Splicing*, *Inpainting*).
- **Multi-Stream Forensic Telemetry**:
  - *Spatial Patches*: DINOv3 ViT-S/16 self-supervised patch tokens with LoRA.
  - *2D FFT Frequency Magnitude*: 2D Fourier polar spectrum diagnosing compression artifacts.
  - *Copy-Move Self-Correlation Map*: Chebyshev distance-masked ( > 1$) mutual affinity matrix isolating cloned regions.
- **Diagnostic Export**:
  - One-click diagnostic executive summary copy to clipboard.
  - Forensic JSON telemetry export.

---

## 🚀 Live Hosting & Deployment Guide

This repository is optimized for instant deployment on **Vercel** and **Render**. Once connected to your GitHub account, **any push to the `main` branch automatically triggers a rebuild and updates the live URL.**

### Option A: Hosting on Vercel (Recommended — Fastest Global CDN)

1. Navigate to [Vercel Dashboard](https://vercel.com/dashboard).
2. Click **Add New...** → **Project**.
3. Select and import the repository: `NEHANGRM/TriForVit-UI`.
4. Configure Project Settings:
   - **Framework Preset**: *Other*
   - **Root Directory**: `./`
   - **Build Command**: *(Leave empty)*
   - **Output Directory**: `./`
5. Click **Deploy**.
6. Within ~15 seconds, your live production URL (e.g., `https://triforvit-ui.vercel.app`) will be active with SSL enabled!

> **Continuous Deployment**: Any future `git push origin main` to `https://github.com/NEHANGRM/TriForVit-UI.git` will automatically deploy your updates to the live Vercel URL.

---

### Option B: Hosting on Render (Static Site)

1. Navigate to the [Render Dashboard](https://dashboard.render.com/).
2. Click **New +** → **Static Site**.
3. Connect your GitHub account and select `NEHANGRM/TriForVit-UI`.
4. Fill in the details:
   - **Name**: `triforvit-ui`
   - **Branch**: `main`
   - **Build Command**: *(Leave empty)*
   - **Publish Directory**: `.`
5. Click **Create Static Site**.
6. Render will generate a live URL (e.g., `https://triforvit-ui.onrender.com`).

> **Render Blueprint**: Alternatively, you can use the included `render.yaml` blueprint file by selecting **New +** → **Blueprint** on Render for zero-click configuration.

---

## 🔌 Connecting Hosted UI to a Live Inference Backend

The web application features a **Hybrid Engine**:
1. **Cloud Interactive Mode (Default)**:
   - All 5 benchmark test cases (*Beach Sailboat Copy-Move*, *Mountain Sky Splicing*, *Inpainted Lake*, *Authentic Mountain*, *Authentic Beach*) are pre-loaded with full high-resolution model inferences, heatmaps, bounding boxes, and frequency streams.
   - Any custom uploaded image is processed via the in-browser forensic canvas filter (Laplacian noise filter + 2D FFT polar magnitude).
2. **Live Backend Mode**:
   - If you run the Python server locally (`python app.py` on your Mac MPS / Linux GPU) or host a dedicated API instance, click the **Backend: Auto** button in the top navigation bar.
   - Enter your backend URL (e.g. `http://127.0.0.1:8000` or an ngrok/Render URL).
   - Click **Save & Connect**. Custom uploaded images will now be processed directly through the full deep PyTorch Vision Transformer model!

---

## 💻 Local Development

To run the UI locally on your computer:

```bash
# Option 1: Python HTTP server
python3 server.py --port 8080

# Option 2: Node npx serve
npx serve . -p 8080
```
Then open `http://localhost:8080` in your web browser.

---

## 📂 Repository File Structure

```text
TriForVit-UI/
├── index.html           # Main single-page forensic web application
├── css/
│   └── style.css        # Responsive dark-mode cyber-forensic design system
├── js/
│   ├── app.js           # Interactive UI logic, sliders, modal & hybrid API client
│   └── demo_data.js     # Precomputed benchmark inference results (FTT v2 model)
├── samples/             # Benchmark test images (JPG)
├── render.yaml          # Render Infrastructure-as-Code Blueprint
├── vercel.json          # Vercel deployment configuration & security headers
├── server.py            # Standalone CORS-enabled Python static server
├── package.json         # NPM metadata and convenience scripts
└── README.md            # Comprehensive project documentation
```

---

## 👥 Authors & Academic Credits

- **Project**: Robust Patch-Based Hierarchical Framework for Image Forgery Detection and Classification
- **Team**: Team 39
- **Course**: Final Year Project (IAPR)
- **Model Engine**: FTT v2 (DINOv3 / ViT + LoRA + Self-Correlation Copy-Move Branch)
