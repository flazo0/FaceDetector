# Real-Time Face Detection System (OpenCV + Haar Cascade)

## Overview

This project implements a **modular, real-time face detection system** using OpenCV and a pre-trained Haar Cascade classifier.

The application captures video frames from a webcam, detects frontal faces, and renders bounding boxes with an interactive HUD overlay. It also includes advanced features such as:

* FPS monitoring
* Screenshot capture
* Video recording
* Camera switching
* Detection strict mode
* CLI-based configuration

The system is designed for educational, experimental, and prototyping purposes in computer vision.

---

## Architecture

The project follows a clean modular structure:

```
FaceDetector/
│
├── app.py                  # Entry point
├── requirements.txt
├── src/
│   ├── config.py           # Configuration dataclasses
│   ├── detector.py         # Face detection logic
│   ├── camera.py           # Camera abstraction
│   ├── overlay.py          # FPS & HUD rendering
│   └── utils.py            # Screenshot & recording utilities
├── models/
│   └── haarcascade_frontalface_default.xml
└── outputs/
    ├── screenshots/
    └── recordings/
```

---

### Core

* Real-time face detection (Haar Cascade)
* Grayscale conversion pipeline
* Bounding box rendering
* Adjustable detection parameters

### Advanced

* Live FPS counter
* Screenshot saving (`S`)
* Video recording (`R`)
* Camera switching (`C`)
* Mirror mode toggle (`M`)
* HUD toggle (`H`)
* Strict detection mode (reduced false positives)
* CLI configuration support

---

## Installation

### Requirements

* Python 3.8+
* OpenCV

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Model Setup

Download the Haar cascade model:

```
haarcascade_frontalface_default.xml
```

From OpenCV official repository:

[https://github.com/opencv/opencv/tree/master/data/haarcascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)

Place it inside:

```
models/
```

---

## Running the Application

Basic run:

```bash
python app.py
```

With custom configuration:

```bash
python app.py --camera 1 --width 1280 --height 720 --strict
```

---

## CLI Arguments

| Argument        | Description                    |
| --------------- | ------------------------------ |
| `--camera`      | Camera index (default: 0)      |
| `--width`       | Capture width                  |
| `--height`      | Capture height                 |
| `--cascade`     | Path to Haar cascade XML       |
| `--scale`       | Detection scale factor         |
| `--neighbors`   | Min neighbors for detection    |
| `--minsize w h` | Minimum detection size         |
| `--no-mirror`   | Disable mirror mode            |
| `--no-fps`      | Disable FPS display            |
| `--strict`      | Enable stricter detection mode |

---

## Keyboard Controls

| Key | Action                     |
| --- | -------------------------- |
| `Q` | Quit                       |
| `H` | Toggle HUD                 |
| `M` | Toggle mirror mode         |
| `S` | Save screenshot            |
| `R` | Start/Stop video recording |
| `C` | Switch camera              |

---

## Detection Pipeline

1. Capture frame from webcam
2. Optional mirror flip
3. Convert to grayscale
4. Apply Haar cascade detection
5. Render bounding boxes
6. Render HUD overlay
7. Display frame

---

## Detection Parameters Explained

### `scaleFactor`

Controls image pyramid scaling.

* Lower → More accurate, slower
* Higher → Faster, less precise

### `minNeighbors`

Controls detection confidence.

* Higher → Fewer false positives
* Lower → More detections (including noise)

### `minSize`

Minimum face size in pixels.

---

## Performance Notes

* CPU-based detection
* No GPU required
* Performance depends on:

  * Frame resolution
  * Lighting conditions
  * CPU capability

For better performance:

* Reduce resolution
* Increase `scaleFactor`
* Enable strict mode

---

## Limitations

* Optimized for frontal faces
* Not robust against:

  * Extreme angles
  * Heavy occlusion
  * Low light
* No face tracking between frames
* Not a face recognition system

---

## Output Artifacts

Screenshots:

```
outputs/screenshots/
```

Recordings:

```
outputs/recordings/
```

---

## Future Improvements

### Detection

* Switch to DNN-based face detection (ResNet / SSD)
* Integrate MediaPipe
* Add face tracking (KCF / CSRT)

### AI Features

* Face recognition (FaceNet / dlib)
* Emotion detection
* Facial landmark extraction

### System Improvements

* Logging system
* Performance benchmarking
* Multi-threaded frame processing
* GPU acceleration (CUDA)
* Config file support (JSON/YAML)

---

## Summary

This project demonstrates a structured, extensible implementation of classical computer vision-based face detection using Haar Cascades.

It provides:

* Clean modular architecture
* CLI configurability
* Real-time processing
* Interactive controls
* Recording and screenshot capabilities

Suitable for learning, experimentation, and as a foundation for more advanced vision systems.