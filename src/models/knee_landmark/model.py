import torch
import torch.nn as nn


class KneeLandmarkModel(nn.Module):
    def __init__(self, num_landmarks=20):
        super().__init__()

        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )

        self.heatmap_head = nn.Sequential(
            nn.Conv2d(256, 128, kernel_size=3, padding=1),
            nn.ReLU(),

            nn.Conv2d(128, num_landmarks, kernel_size=1)
        )

    def forward(self, x):
        x = self.features(x)
        return self.heatmap_head(x)


if __name__ == "__main__":
    model = KneeLandmarkModel()

    x = torch.randn(2, 3, 256, 256)
    output = model(x)

    print("Input shape :", x.shape)
    print("Output shape:", output.shape)