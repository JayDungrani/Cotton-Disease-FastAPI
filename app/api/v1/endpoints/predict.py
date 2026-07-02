from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.schemas.prediction import PredictionResponse
from app.services.predictor import CottonDiseasePredictor
from app.api import deps

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict_cotton_disease(
    file: UploadFile = File(...),
    predictor: CottonDiseasePredictor = Depends(deps.get_predictor)
):
    # Validate it's an image file format
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File provided is not an image.")
        
    image_bytes = await file.read()
    
    try:
        prediction = predictor.predict(image_bytes)
        return {
            "filename": file.filename,
            "predicted_class": prediction["predicted_class"],
            "confidence": prediction["confidence"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference failed: {str(e)}")