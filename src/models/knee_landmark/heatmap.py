import math
import torch


def generate_heatmap(x, y, height=32, width=32, sigma=1.5):
    heatmap = torch.zeros(height, width)

    for i in range(height):
        for j in range(width):
            heatmap[i, j] = math.exp(
                -((j - x) ** 2 + (i - y) ** 2) / (2 * sigma ** 2)
            )

    return heatmap


def generate_landmark_heatmaps(landmarks, height=32, width=32, sigma=1.5):
    heatmaps = torch.zeros(len(landmarks), height, width)

    for i, (x, y) in enumerate(landmarks):
        heatmaps[i] = generate_heatmap(
            x, y, height, width, sigma
        )

    return heatmaps


if __name__ == "__main__":
    landmarks = [
        (10, 15),
        (20, 12),
        (8, 25),
        (16, 16)
    ]

    heatmaps = generate_landmark_heatmaps(landmarks)

    print("Input landmarks :", len(landmarks))
    print("Output shape    :", heatmaps.shape)
    print("Maximum value   :", heatmaps.max().item())