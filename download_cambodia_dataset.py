"""
Cambodian Road & Traffic Sign Dataset Setup Helper.
Allows downloading via Roboflow API or generating starter test dataset.
"""

import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TARGET_DATASET_DIR = BASE_DIR / "road_detection_model" / "cambodia_road_detection"


def download_with_roboflow(api_key, workspace_name="cambodia-traffic-signs", project_name="cambodia-road-signs", version=1):
    try:
        from roboflow import Roboflow
    except ImportError:
        print("[ERROR] Roboflow package not installed. Run: pip install roboflow")
        return False

    try:
        print(f"\n[INFO] Connecting to Roboflow workspace '{workspace_name}'...")
        rf = Roboflow(api_key=api_key)
        project = rf.workspace(workspace_name).project(project_name)
        v = project.version(version)
        TARGET_DATASET_DIR.mkdir(parents=True, exist_ok=True)
        print(f"[INFO] Downloading YOLOv8 dataset to: {TARGET_DATASET_DIR}")
        dataset = v.download("yolov8", location=str(TARGET_DATASET_DIR))
        print(f"[SUCCESS] Dataset successfully downloaded to: {TARGET_DATASET_DIR}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to download from Roboflow: {e}")
        return False


def generate_starter():
    from road_detection_model.train import generate_starter_cambodia_dataset
    generate_starter_cambodia_dataset(TARGET_DATASET_DIR)


def print_manual_guide():
    print("\n" + "="*60)
    print("      MANUAL DOWNLOAD GUIDE FOR CAMBODIA DATASET")
    print("="*60)
    print("1. Open Roboflow Universe in your browser:")
    print("   https://universe.roboflow.com/search?q=cambodia+traffic+signs")
    print("   (Or any ASEAN / Southeast Asia traffic sign dataset)")
    print("\n2. Select a dataset, click 'Download Dataset'")
    print("   - Select Format: YOLOv8")
    print("   - Select: 'Download zip to computer'")
    print("\n3. Extract the downloaded .zip into this exact folder:")
    print(f"   {TARGET_DATASET_DIR}\\")
    print("   Verify it contains:")
    print("     train/images/ & train/labels/")
    print("     valid/images/ & valid/labels/")
    print("     data.yaml")
    print("="*60 + "\n")


def main():
    print("\n" + "="*50)
    print("   CAMBODIAN ROAD SIGN DATASET SETUP")
    print("="*50)
    print("1. Enter Roboflow API Key to download automatically")
    print("2. Generate starter mock dataset (for immediate testing)")
    print("3. View manual download & extraction instructions")
    print("4. Exit")
    print("="*50)

    choice = input("Enter choice [1-4]: ").strip()

    if choice == '1':
        key = input("Enter Roboflow API Key: ").strip()
        workspace = input("Workspace name (default: cambodia-traffic-signs): ").strip() or "cambodia-traffic-signs"
        proj = input("Project name (default: cambodia-road-signs): ").strip() or "cambodia-road-signs"
        if key:
            download_with_roboflow(key, workspace, proj)
    elif choice == '2':
        generate_starter()
    elif choice == '3':
        print_manual_guide()
    else:
        print("Exiting.")


if __name__ == "__main__":
    main()
