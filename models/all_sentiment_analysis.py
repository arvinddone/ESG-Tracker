import pandas as pd
from textblob import TextBlob

df = pd.read_csv(
    "data/all_esg_results.csv"
)

sentiments = []

for article in df["Article"]:

    article = str(article)

    polarity = (
        TextBlob(article)
        .sentiment
        .polarity
    )

    if polarity > 0:

        sentiment = "Positive"

    elif polarity < 0:

        sentiment = "Negative"

    else:

        sentiment = "Neutral"

    sentiments.append(
        sentiment
    )

df["Sentiment"] = sentiments

df.to_csv(
    "data/all_esg_sentiment.csv",
    index=False
)

print(
    "Sentiment Analysis Completed!"
)

print(
    df["Sentiment"]
    .value_counts()
)
