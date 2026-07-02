import sys
from pathlib import Path

# 1. Get the absolute path of the directory containing run_inference.py
current_dir = Path(__file__).resolve().parent

# 2. Get the path of the parent directory (my_project/)
parent_dir = current_dir.parent

# 3. Add the parent directory to Python's search path if it's not already there
if str(parent_dir) not in sys.path:
    sys.path.append(str(parent_dir))

from app.services.predictor import CottonDiseasePredictor

model_file = Path("models") / "best_cotton_resnet.pt" #model filename
class_file = Path("models") / "class_map.json" #test image filename
test_img_file = Path("tests") / "curl00.jpg"

predictor = CottonDiseasePredictor(
    model_path=str(model_file), 
    class_map_path=str(class_file)
)

with open(test_img_file, "rb") as f:
    image_bytes = f.read()

result = predictor.predict(image_bytes=image_bytes)
print(result)