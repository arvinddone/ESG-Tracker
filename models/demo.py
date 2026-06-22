import pandas as pd

df = pd.read_csv("data/all_headlines.csv")

print("\nTCS Headlines:\n")

print(
    df[df["Company"] == "TCS"]
    .head(10)
)