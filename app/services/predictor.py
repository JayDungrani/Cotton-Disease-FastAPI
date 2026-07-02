import io
import json
from PIL import Image
import torch
import torchvision.transforms as transforms
import torchvision.models as models

class CottonDiseasePredictor:
    def __init__(self, model_path:str, class_map_path:str):

        # class map
        with open(class_map_path, "r") as f:
            self.class_map = json.load(f)
        
        # transform input
        self.transforms = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor()
        ])

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        weights = models.ResNet50_Weights.DEFAULT
        self.model = models.resnet50(weights=weights)

        num_classes = len(self.class_map)
        self.model.fc = torch.nn.Linear(self.model.fc.in_features, num_classes)
    
        state_dict = torch.load(model_path, map_location=self.device)
        self.model.load_state_dict(state_dict)
        self.model.to(self.device)

        self.model.eval()
    
    def predict(self, image_bytes:bytes):
        
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        tensor = self.transforms(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            outputs = self.model(tensor)
            probablities = torch.nn.functional.softmax(outputs[0], dim=0)

            confidence, class_idx = torch.max(probablities, dim=0)
            class_str = str(class_idx.item())
        
        return {
            "predicted_class" : self.class_map.get(class_str),
            "confidence" : float(confidence.item())
        }

        