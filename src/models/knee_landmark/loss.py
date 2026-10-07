import torch
import torch.nn as nn


class HeatmapLoss(nn.Module):
    def __init__(self):
        super().__init__()
        self.loss = nn.MSELoss()

    def forward(self, predicted, target):
        return self.loss(predicted, target)


if __name__ == "__main__":
    criterion = HeatmapLoss()

    predicted = torch.randn(2, 20, 32, 32)
    target = torch.randn(2, 20, 32, 32)

    loss = criterion(predicted, target)

    print("Predicted shape:", predicted.shape)
    print("Target shape   :", target.shape)
    print("Loss           :", loss.item())