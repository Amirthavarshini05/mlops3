from sklearn.metrics import f1_score

y_true = [1,1,1,0,0,1,0,1,1,0]
y_pred = [1,1,1,0,0,1,0,1,1,0]

f1 = f1_score(y_true, y_pred)
print(f"F1 Score: {f1:.2f}")

if f1 < 0.85:
    raise SystemExit("F1 gate failed.")

print("F1 gate passed.")
