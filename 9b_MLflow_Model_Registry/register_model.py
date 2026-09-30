import os
import mlflow
from mlflow.tracking import MlflowClient

tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000")
run_id = os.getenv("BEST_RUN_ID", "")
model_name = os.getenv("MODEL_NAME", "WineQualityModel")
threshold = 0.80

if not run_id:
    raise SystemExit("Set BEST_RUN_ID to the best run from Question 7.")

mlflow.set_tracking_uri(tracking_uri)
client = MlflowClient()

run = client.get_run(run_id)
accuracy = run.data.metrics.get("accuracy", 0.0)

print("Run:", run_id)
print("Accuracy:", accuracy)

if accuracy <= threshold:
    raise SystemExit(f"Validation failed: accuracy {accuracy} <= {threshold}")

model_uri = f"runs:/{run_id}/model"
result = mlflow.register_model(model_uri, model_name)

version = result.version
print("Registered version:", version)

client.update_model_version(
    name=model_name,
    version=version,
    description="Wine Quality model selected from Exp 7"
)

client.set_model_version_tag(model_name, version, "source_run", run_id)
client.set_model_version_tag(model_name, version, "validation", "passed")

client.transition_model_version_stage(
    name=model_name,
    version=version,
    stage="Staging",
    archive_existing_versions=False
)

client.transition_model_version_stage(
    name=model_name,
    version=version,
    stage="Production",
    archive_existing_versions=True
)

print("Model moved to Production.")

model = mlflow.sklearn.load_model(f"models:/{model_name}/Production")
print("Production model loaded.")

# Example batch input from the Wine Quality feature columns.
import pandas as pd
data = pd.read_csv(
    "https://raw.githubusercontent.com/selva86/datasets/master/WineQuality_Red.csv"
)
X_batch = data.drop("quality", axis=1).head(10)
predictions = model.predict(X_batch)
print("Batch predictions:", predictions)
