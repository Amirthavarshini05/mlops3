# 7b - MLflow Wine Quality Experiment

Install:
pip install -r requirements.txt

Run:
python wine_mlflow.py

Start UI:
mlflow ui

Open:
http://127.0.0.1:5000

The script trains Logistic Regression, Random Forest and XGBoost.
It logs parameters, Accuracy, F1, ROC-AUC, confusion matrices and models.
Finally it uses MlflowClient.search_runs to select the run with highest Accuracy.
