# Cotton Disease Prediction API 🌿🤖

A production-ready, highly optimized FastAPI application that leverages a PyTorch Deep Learning model to predict diseases in cotton leaves from uploaded images. 

---

## 🚀 Features
* **FastAPI Web Framework:** High performance, easy to use, and automatically generates interactive Swagger documentation.
* **PyTorch Inference Layer:** Configured for highly efficient CPU-based matrix operations.
* **Optimized Docker Configuration:** Uses a multi-stage build system to reduce the image footprint to under 1GB (handling the heavy PyTorch framework efficiently).
* **Dependency Injection:** The 90 MB PyTorch model is loaded once into memory at application startup, avoiding overhead on sequential requests.

---

## 📂 Project Structure

```text
cotton-disease-api/
├── app/
│   ├── api/                     # Routing & Endpoint logic
│   │   ├── deps.py              # Dependencies (Model instance injection)
│   │   └── v1/endpoints/        # v1 API Routes (/predict)
│   ├── core/config.py           # App configuration settings
│   ├── schemas/prediction.py    # Pydantic data validation contracts
│   └── services/predictor.py    # PyTorch data pipeline & forward pass logic
├── models/
│   ├── class_map.json           # Index-to-string dictionary maps
│   └── cotton_model.pt          # PyTorch Model weights (~90 MB)
├── Dockerfile                   # Optimized multi-stage production Dockerfile
├── requirements.txt             # Strict CPU-optimized dependency locks
└── README.md
```

## 🛠️ Local Development Setup
1. Prerequisites
Ensure you have Python 3.11+ installed on your local machine.

2. Installation
Clone the repository, set up a virtual environment, and install the locked CPU dependencies:
```text
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies (utilizes the custom PyTorch CPU index wheels)
pip install -r requirements.txt
```
3. Running the API Locally
Start the local development server using Uvicorn:
```text
uvicorn app.main:app --reload
```
## 🐳 Docker Deployment (Production)
The containerization workflow uses a multi-stage pipeline that installs isolated CPU-only wheels, stripping away heavy compilation caches and dependencies.

1. Build the Production Image
Run the build command from the root directory:
```
docker build -t cotton-disease-api:v1 .
```
2. Run the Containerized App
Forward host port 8000 into the container's exposed port 8000:
```docker run -d -p 8000:8000 --name cotton-app cotton-disease-api:v1```

##📋 API Reference
Predict Cotton Disease
Accepts a raw image upload payload via multipart form-data.
```
Endpoint: POST /api/v1/predict
Content-Type: multipart/form-data
Payload: file: <Image Binary>
```
Expected JSON Response Contract:
```
{
  "filename": "healthy_leaf.jpg",
  "predicted_class": "Healthy Cotton Leaf",
  "confidence": 0.9421
}
```
