import torch


def decode_heatmaps(heatmaps):
    num_landmarks, height, width = heatmaps.shape

    landmarks = []

    for i in range(num_landmarks):
        heatmap = heatmaps[i]

        confidence, index = torch.max(heatmap.view(-1), dim=0)

        y = index // width
        x = index % width

        landmarks.append({
            "id": i + 1,
            "x": x.item(),
            "y": y.item(),
            "confidence": confidence.item()
        })

    return landmarks


if __name__ == "__main__":
    heatmaps = torch.zeros(20, 32, 32)

    heatmaps[0, 10, 15] = 1.0
    heatmaps[1, 20, 25] = 0.8

    landmarks = decode_heatmaps(heatmaps)

    for landmark in landmarks[:2]:
        print(landmark)