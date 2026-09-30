from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI(title="Student Performance Prediction API")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

class PredictionInput(BaseModel):
    features: list[float]

@app.get("/health")
def health():
    return {"status": "healthy", "model_version": "1.0"}

@app.post("/predict")
def predict(data: PredictionInput):
    score = sum(data.features) / len(data.features)
    prediction = "Positive" if score >= model["threshold"] else "Negative"
    confidence = min(0.99, 0.50 + abs(score - model["threshold"]) * 0.05)
    return {
        "prediction": prediction,
        "confidence": round(confidence, 2)
    }
