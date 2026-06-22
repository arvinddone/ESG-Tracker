import pandas as pd

df = pd.read_csv("data/all_articles.csv")

categories = []

for article in df["Article"]:

    article = str(article).lower()

    if any(word in article for word in
           ["renewable", "solar", "green", "emission", "sustainability"]):

        category = "Environmental"

    elif any(word in article for word in
             ["employee", "worker", "labour", "diversity", "workplace"]):

        category = "Social"

    elif any(word in article for word in
             ["fraud", "corruption", "governance", "board", "compliance"]):

        category = "Governance"

    else:

        category = "Financial / Other"

    categories.append(category)

df["ESG_Category"] = categories

df.to_csv(
    "data/all_esg_results.csv",
    index=False
)

print("Classification Completed!")

print("\nCategory Counts:\n")
print(df["ESG_Category"].value_counts())