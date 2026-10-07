import csv
from pathlib import Path

import torch
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms

from heatmap import generate_landmark_heatmaps


class KneeLandmarkDataset(Dataset):
    def __init__(self, annotation_file, image_size=256, heatmap_size=32):
        self.annotation_file = Path(annotation_file)
        self.image_size = image_size
        self.heatmap_size = heatmap_size

        self.samples = []

        with open(self.annotation_file, newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                self.samples.append(row)

        self.transform = transforms.Compose([
            transforms.Resize((image_size, image_size)),
            transforms.ToTensor()
        ])

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        row = self.samples[index]

        image_path = row[0]

        image = Image.open(image_path).convert("RGB")

        original_width, original_height = image.size

        landmarks = []

        for i in range(20):
            x = float(row[1 + i * 2])
            y = float(row[2 + i * 2])

            x = x * self.image_size / original_width
            y = y * self.image_size / original_height

            landmarks.append((x, y))

        image = self.transform(image)

        scale = self.heatmap_size / self.image_size

        heatmap_landmarks = [
            (x * scale, y * scale)
            for x, y in landmarks
        ]

        heatmaps = generate_landmark_heatmaps(
            heatmap_landmarks,
            self.heatmap_size,
            self.heatmap_size
        )

        return image, heatmaps


if __name__ == "__main__":
    print("KneeLandmarkDataset ready.")