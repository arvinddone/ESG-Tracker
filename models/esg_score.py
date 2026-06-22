import pandas as pd

df = pd.read_csv("data/infosys_esg_sentiment.csv")

score = 50   # Base Score

for _, row in df.iterrows():

    category = row["ESG_Category"]
    sentiment = row["Sentiment"]

    if category == "Environmental":

        if sentiment == "Positive":
            score += 5
        elif sentiment == "Negative":
            score -= 5

    elif category == "Social":

        if sentiment == "Positive":
            score += 4
        elif sentiment == "Negative":
            score -= 4

    elif category == "Governance":

        if sentiment == "Positive":
            score += 6
        elif sentiment == "Negative":
            score -= 6

# Score Limit
score = max(0, min(score, 100))

print("\n========================")
print("COMPANY : INFOSYS")
print("========================")
print(f"Overall ESG Score : {score}/100")
print("========================")
