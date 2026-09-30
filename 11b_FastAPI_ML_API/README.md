# 11b - FastAPI + Pydantic + AsyncClient + Docker

Install:
pip install -r requirements.txt

Test:
pytest -v

Run:
uvicorn app.main:app --reload

Swagger:
http://127.0.0.1:8000/docs

Docker:
docker build -t fastapi-ml-tests .
docker run --rm fastapi-ml-tests

The Dockerfile runs the pytest integration tests.
