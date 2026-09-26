# 🇰🇭 Cambodia Road & Traffic Sign Detection with YOLOv8

An AI-powered computer vision system fine-tuned to detect Cambodian road signs, traffic lights, and local road objects (such as Tuk-Tuks, PassApps, motorcycles, stop signs, warning signs, speed limits, and pedestrian crossings).

---

## 🚀 Quick Start (Interactive Menu)

Run the interactive launcher to access all features:
```bash
python run.py
```
*(or with Poetry: `python -m poetry run python run.py`)*

Options available in the menu:
1. **Live Detection on Video**: Runs detection on sample driving video (`test_film.mp4`)
2. **Live Detection on Webcam**: Detects objects in real-time from your camera
3. **Custom Video/Image**: Point to any file for instant detection
4. **Train / Fine-tune for Cambodia**: Trains YOLOv8 on Cambodian road sign dataset
5. **Validate Model**: Evaluates mAP@50, Precision, Recall, and F1-score
6. **Download Roboflow Dataset**: Download official Cambodia road sign dataset via Roboflow API
7. **Generate Starter Dataset**: Quickly creates starter mock data to verify training pipeline

---

## 🎯 Command Line Usage

### 1. Live Detection
```bash
# Detect on video
python road_detection_model/live.py --source test_images/test_film.mp4 --conf 0.20

# Detect on webcam
python road_detection_model/live.py --source 0

# Detect on a photo/image
python road_detection_model/live.py --source my_road_photo.jpg
```

**Live Keyboard Controls:**
- `Space`: Pause / Resume playback
- `s`: Save snapshot/screenshot of the current frame to `runs/screenshots/`
- `+` / `-`: Increase or decrease confidence threshold dynamically
- `q`: Exit

### 2. Fine-Tuning for Cambodia Road Signs
```bash
# Fine-tune model using transfer learning from fine_tuned_yolov8s.pt
python road_detection_model/train.py --stage cambodia --epochs 50 --batch 8

# Generate starter test dataset to test pipeline right away
python road_detection_model/train.py --generate-starter
```

### 3. Model Validation
```bash
# Validate accuracy and calculate mAP
python road_detection_model/validate.py --stage cambodia
```

---

## 🏷️ Supported Cambodian Road Classes

- `car`
- `motorcycle`
- `tuk-tuk` / `passapp`
- `pedestrian`
- `traffic light` (red, green)
- `stop sign` (ឈប់)
- `speed limit sign` (ល្បឿនកំណត់)
- `prohibition sign` (សញ្ញាហាមឃាត់)
- `warning sign` (សញ្ញាគ្រោះថ្នាក់)
- `mandatory sign` (សញ្ញាបញ្ជា)
- `pedestrian crossing` (គំនូសសេះបង្កង់)
- `priority sign`

---

## 📦 Dataset Setup

To train with real Cambodian traffic signs:
1. Visit [Roboflow Universe: Cambodia Traffic Signs](https://universe.roboflow.com/search?q=cambodia+traffic+signs).
2. Download in **YOLOv8** format.
3. Unzip into `road_detection_model/road_detection_model/cambodia_road_detection/`.
4. Run `python road_detection_model/train.py --stage cambodia`.
