import pandas as pd

df = pd.read_csv("data/infosys_articles.csv")

article = df.loc[0, "Article"].lower()

if any(word in article for word in ["renewable", "solar", "green", "emission"]):
    category = "Environmental"

elif any(word in article for word in ["employee", "worker", "labour", "diversity"]):
    category = "Social"

elif any(word in article for word in ["fraud", "corruption", "governance", "board"]):
    category = "Governance"

else:
    category = "Financial / Other"

print("ESG Category:", category)