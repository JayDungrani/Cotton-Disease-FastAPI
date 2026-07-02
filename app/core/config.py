from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_PATH: str = "models/best_cotton_resnet.pt"
    CLASS_MAP_PATH: str = "models/class_map.json"

settings = Settings()