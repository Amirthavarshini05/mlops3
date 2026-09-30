import pytest
from httpx import ASGITransport, AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_health():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["model_version"] == "1.0.0"

@pytest.mark.asyncio
async def test_model_info():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/model-info")
    assert response.status_code == 200
    assert response.json()["status"] == "loaded"

@pytest.mark.asyncio
async def test_predict():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/predict", json={"features": [6, 7, 8]})
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] == "Positive"
    assert 0 <= data["confidence"] <= 1

@pytest.mark.asyncio
async def test_invalid_prediction_input():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/predict", json={"features": []})
    assert response.status_code == 422
