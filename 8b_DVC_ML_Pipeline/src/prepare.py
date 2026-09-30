import pandas as pd
df = pd.read_csv("data/books.csv")
df = df.dropna()
df.to_csv("data/prepared.csv", index=False)
print("Data preparation completed.")
