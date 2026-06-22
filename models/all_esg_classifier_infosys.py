import pandas as pd

df = pd.read_csv("data/infosys_all_articles.csv")

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
    "data/infosys_esg_results.csv",
    index=False
)

print("ESG Classification Completed!")
print(df["ESG_Category"].value_counts())