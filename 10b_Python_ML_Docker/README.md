# 10b - Multi-stage Python ML API Dockerfile

Build:
docker build -t python-ml-api:1.0 .

Run:
docker run -d --name python-ml-api -p 8000:8000 python-ml-api:1.0

Health:
curl http://localhost:8000/health

Prediction Windows CMD:
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d "{\"features\":[6,7,8]}"

Push:
docker tag python-ml-api:1.0 YOUR_USERNAME/python-ml-api:1.0
docker push YOUR_USERNAME/python-ml-api:1.0
