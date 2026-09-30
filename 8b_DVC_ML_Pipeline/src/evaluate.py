import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("data/prepared.csv")
X = df[["pages"]]
y = df["price"]

model = joblib.load("model.pkl")
pred = model.predict(X)

mse = mean_squared_error(y, pred)
r2 = r2_score(y, pred)

with open("metrics.txt", "w") as f:
    f.write(f"mse: {mse}\n")
    f.write(f"r2: {r2}\n")

print("MSE:", mse)
print("R2:", r2)
