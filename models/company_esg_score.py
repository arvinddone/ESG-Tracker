import pandas as pd

df = pd.read_csv(
    "data/all_esg_sentiment.csv"
)

results = []

companies = df["Company"].unique()

for company in companies:

    company_df = df[
        df["Company"] == company
    ]

    # Financial / Other articles ignore
    esg_df = company_df[
        company_df["ESG_Category"]
        != "Financial / Other"
    ]

    positive_esg = len(
        esg_df[
            esg_df["Sentiment"]
            == "Positive"
        ]
    )

    negative_esg = len(
        esg_df[
            esg_df["Sentiment"]
            == "Negative"
        ]
    )

    total = positive_esg + negative_esg

    if total == 0:

        score = 50

    else:

        raw_score = (
            positive_esg / total
        ) * 100

        score = round(
            50 + (raw_score * 0.45),
            2
        )

    results.append({

        "Company": company,

        "Positive_ESG": positive_esg,

        "Negative_ESG": negative_esg,

        "ESG_Score": score

    })

result_df = pd.DataFrame(
    results
)

result_df.to_csv(
    "data/company_esg_scores.csv",
    index=False
)

print("\nCompany ESG Scores\n")

print(
    result_df.sort_values(
        by="ESG_Score",
        ascending=False
    )
)