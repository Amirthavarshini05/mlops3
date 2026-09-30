# 9b - Register Best Model from Exp 7

This script expects an MLflow run ID from Question 7.

Set environment variables:
Windows CMD:
set MLFLOW_TRACKING_URI=http://127.0.0.1:5000
set BEST_RUN_ID=YOUR_RUN_ID
set MODEL_NAME=WineQualityModel

Then:
python register_model.py

The lab requires:
None -> Staging -> Production
with a validation gate based on accuracy.

Note: newer MLflow versions increasingly recommend model aliases; this folder follows
the stage-based workflow required by the lab question.
