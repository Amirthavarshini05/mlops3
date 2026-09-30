MODEL_VERSION = "1.0.0"

def predict_model(features):
    score = sum(features) / len(features)
    prediction = "Positive" if score >= 5 else "Negative"
    confidence = min(0.99, 0.50 + abs(score - 5) * 0.05)
    return prediction, round(confidence, 2)
