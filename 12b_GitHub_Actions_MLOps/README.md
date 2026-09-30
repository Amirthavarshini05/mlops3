# 12b - GitHub Actions 4-job MLOps Pipeline

Jobs:
1. data-validation - Great Expectations
2. train-and-evaluate - F1 gate >= 0.85
3. build-docker - image tagged with Git SHA
4. deploy-staging - kubectl apply

Jobs run sequentially using `needs`.

The deploy job assumes Kubernetes credentials/context are configured in GitHub Actions.
For a real deployment, the Docker image should be pushed to a registry and the Kubernetes
Deployment should reference that registry image.
