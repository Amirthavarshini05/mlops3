from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.model import predict_model, MODEL_VERSION

app = FastAPI(title="ML Prediction API", version=MODEL_VERSION)

class PredictionInput(BaseModel):
    features: list[float] = Field(..., min_length=1)

@app.get("/health")
async def health():
    return {"status": "healthy", "model_version": MODEL_VERSION}

@app.get("/model-info")
async def model_info():
    return {
        "model_name": "Simple Classification Model",
        "model_version": MODEL_VERSION,
        "framework": "Python/FastAPI",
        "status": "loaded"
    }

@app.post("/predict")
async def predict(data: PredictionInput):
    prediction, confidence = predict_model(data.features)
    return {
        "prediction": prediction,
        "confidence": confidence,
        "model_version": MODEL_VERSION
    }
