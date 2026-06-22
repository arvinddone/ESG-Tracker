import pandas as pd
from textblob import TextBlob

# ESG results file वाचा
df = pd.read_csv("data/infosys_esg_results.csv")

sentiments = []

for article in df["Article"]:

    article = str(article)

    # Sentiment Score
    polarity = TextBlob(article).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"

    elif polarity < 0:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    sentiments.append(sentiment)

# नवीन column add करा
df["Sentiment"] = sentiments

# Save new file
df.to_csv(
    "data/infosys_esg_sentiment.csv",
    index=False
)

print("\nSentiment Analysis Completed!\n")

# Count Summary
print(df["Sentiment"].value_counts())