from fastapi import FastAPI
from app.api.v1.api import api_router

app = FastAPI(title="Cotton Disease Prediction API", version="1.0.0")

# Include all the v1 routes under /api/v1
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Cotton Disease Prediction API. Go to /docs for Swagger UI."}