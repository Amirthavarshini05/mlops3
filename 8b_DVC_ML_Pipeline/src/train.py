import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("data/prepared.csv")
X = df[["pages"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)
joblib.dump(model, "model.pkl")
print("Model training completed.")
