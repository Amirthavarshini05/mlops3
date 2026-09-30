import mlflow
import mlflow.sklearn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from mlflow.tracking import MlflowClient
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, confusion_matrix
from xgboost import XGBClassifier

DATA_URL = "https://raw.githubusercontent.com/selva86/datasets/master/WineQuality_Red.csv"
EXPERIMENT = "Wine Quality Classification"

data = pd.read_csv(DATA_URL)
data["quality"] = (data["quality"] >= 7).astype(int)

X = data.drop("quality", axis=1)
y = data["quality"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

mlflow.set_experiment(EXPERIMENT)

models = {
    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ]),
    "Random Forest": RandomForestClassifier(
        n_estimators=100, max_depth=10, random_state=42
    ),
    "XGBoost": XGBClassifier(
        n_estimators=100, max_depth=5, learning_rate=0.1,
        random_state=42, eval_metric="logloss"
    )
}

for name, model in models.items():
    with mlflow.start_run(run_name=name):
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        prob = model.predict_proba(X_test)[:, 1]

        accuracy = accuracy_score(y_test, pred)
        f1 = f1_score(y_test, pred)
        roc_auc = roc_auc_score(y_test, prob)

        mlflow.log_param("model_name", name)
        if name == "Random Forest":
            mlflow.log_params({"n_estimators": 100, "max_depth": 10})
        elif name == "XGBoost":
            mlflow.log_params({
                "n_estimators": 100,
                "max_depth": 5,
                "learning_rate": 0.1
            })

        mlflow.log_metrics({
            "accuracy": accuracy,
            "f1": f1,
            "roc_auc": roc_auc
        })

        cm = confusion_matrix(y_test, pred)
        plt.figure(figsize=(5, 4))
        sns.heatmap(cm, annot=True, fmt="d")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.title(f"{name} Confusion Matrix")
        filename = name.replace(" ", "_") + "_confusion_matrix.png"
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()

        mlflow.log_artifact(filename)
        mlflow.sklearn.log_model(model, "model")

client = MlflowClient()
experiment = client.get_experiment_by_name(EXPERIMENT)
runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["metrics.accuracy DESC"]
)

best = runs[0]
print("\nBest Model")
print("Run ID:", best.info.run_id)
print("Model:", best.data.params["model_name"])
print("Accuracy:", best.data.metrics["accuracy"])
print("F1:", best.data.metrics["f1"])
print("ROC-AUC:", best.data.metrics["roc_auc"])
