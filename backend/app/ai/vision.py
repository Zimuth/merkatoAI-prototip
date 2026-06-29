import torch
from torchvision import models, transforms
from PIL import Image

model = models.resnet50(
    weights="DEFAULT"
)
model.eval()
weights = models.ResNet50_Weights.DEFAULT
labels = weights.meta["categories"]
transform = weights.transforms()

def analyze_image(
    image_path:str
):
    image = Image.open(
        image_path
    ).convert("RGB")
    tensor = transform(
        image
    )
    tensor = tensor.unsqueeze(0)
    with torch.no_grad():
        output = model(
            tensor
        )
    probabilities = torch.nn.functional.softmax(
        output[0],
        dim=0
    )
    confidence, index = torch.max(
        probabilities,
        0
    )
    return {
        "suggested_name":
        labels[index],
        "category":
        labels[index],
        "confidence":
        round(
            confidence.item(),
            4
        )
    }