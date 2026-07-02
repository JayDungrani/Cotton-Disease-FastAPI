from app.services.predictor import CottonDiseasePredictor
from app.core.config import settings

# Global variable to hold our loaded predictor single instance
_predictor = None

def get_predictor() -> CottonDiseasePredictor:
    global _predictor
    if _predictor is None:
        _predictor = CottonDiseasePredictor(
            model_path=settings.MODEL_PATH,
            class_map_path=settings.CLASS_MAP_PATH
        )
    return _predictor