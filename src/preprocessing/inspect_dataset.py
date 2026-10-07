import os
from pathlib import Path
from PIL import Image

DATA_DIR = Path("data/raw")

image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}
video_extensions = {".mp4", ".avi", ".mov", ".mkv"}
annotation_extensions = {".json", ".csv", ".xml", ".txt", ".yaml", ".yml"}

images = []
videos = []
annotations = []

for path in DATA_DIR.rglob("*"):
    if not path.is_file():
        continue

    ext = path.suffix.lower()

    if ext in image_extensions:
        images.append(path)
    elif ext in video_extensions:
        videos.append(path)
    elif ext in annotation_extensions:
        annotations.append(path)

print("\nDATASET SUMMARY")
print("-" * 40)

print(f"Images      : {len(images)}")
print(f"Videos      : {len(videos)}")
print(f"Annotations : {len(annotations)}")

if images:
    print("\nIMAGE SAMPLES")
    print("-" * 40)

    for path in images[:10]:
        try:
            with Image.open(path) as img:
                print(f"{path} -> {img.size} {img.mode}")
        except Exception as e:
            print(f"{path} -> ERROR: {e}")

if videos:
    print("\nVIDEO SAMPLES")
    print("-" * 40)

    for path in videos[:10]:
        print(path)

if annotations:
    print("\nANNOTATION FILES")
    print("-" * 40)

    for path in annotations[:20]:
        print(path)