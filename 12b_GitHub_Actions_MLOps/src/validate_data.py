import pandas as pd

df = pd.read_csv("data/students.csv")
required = ["student_id", "attendance", "result"]

for col in required:
    if col not in df.columns:
        raise ValueError(f"Missing column: {col}")

if df.isnull().sum().sum() > 0:
    raise ValueError("Dataset contains missing values")

print("Basic data validation successful.")
