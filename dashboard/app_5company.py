# ESG MULTI COMPANY DASHBOARD

import streamlit as st
import pandas as pd
import plotly.express as px


# PAGE SETTINGS

st.set_page_config(
    page_title="ESG Intelligence Dashboard",
    layout="wide"
)


# LOAD DATA


# Company ESG Scores
scores_df = pd.read_csv(
    "data/company_esg_scores.csv"
)

# Articles + ESG + Sentiment
articles_df = pd.read_csv(
    "data/all_esg_sentiment.csv"
)


# TITLE

st.title("🌍 ESG Intelligence Dashboard")

st.write(
    "Track ESG performance using "
    "news scraping, sentiment analysis "
    "and ESG classification."
)


# COMPANY DROPDOWN

selected_company = st.selectbox(
    "Select Company",
    scores_df["Company"]
)

# SELECTED COMPANY DATA


company_score = scores_df[
    scores_df["Company"]
    == selected_company
]

score = company_score[
    "ESG_Score"
].values[0]


# RISK LEVEL

if score >= 90:
    risk = "🟢 Low Risk"

elif score >= 75:
    risk = "🟡 Medium Risk"

else:
    risk = "🔴 High Risk"


# KPI CARDS


st.write("## ESG Overview")

col1, col2 = st.columns(2)

col1.metric(
    "ESG Score",
    score
)

col2.metric(
    "Risk Level",
    risk
)


# FILTER ARTICLES

company_articles = articles_df[
    articles_df["Company"]
    == selected_company
]


# SENTIMENT COUNTS

positive = len(
    company_articles[
        company_articles["Sentiment"]
        == "Positive"
    ]
)

neutral = len(
    company_articles[
        company_articles["Sentiment"]
        == "Neutral"
    ]
)

negative = len(
    company_articles[
        company_articles["Sentiment"]
        == "Negative"
    ]
)


# SENTIMENT METRICS

st.write("## Sentiment Summary")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Positive",
    positive
)

c2.metric(
    "Neutral",
    neutral
)

c3.metric(
    "Negative",
    negative
)


# PIE CHART
sentiment_df = pd.DataFrame({

    "Sentiment": [
        "Positive",
        "Neutral",
        "Negative"
    ],

    "Count": [
        positive,
        neutral,
        negative
    ]

})

fig = px.pie(

    sentiment_df,

    names="Sentiment",

    values="Count",

    title="Sentiment Distribution"

)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ESG CATEGORY DISTRIBUTION

st.write(
    "## ESG Category Distribution"
)

category_counts = (
    company_articles["ESG_Category"]
    .value_counts()
    .reset_index()
)

category_counts.columns = [
    "Category",
    "Count"
]

fig2 = px.bar(

    category_counts,

    x="Category",

    y="Count",

    title="ESG Categories"

)

st.plotly_chart(
    fig2,
    use_container_width=True
)


# RECENT ARTICLES TABLE

st.write(
    "## Recent Articles"
)

st.dataframe(

    company_articles[

        [
            "Title",
            "ESG_Category",
            "Sentiment"
        ]

    ],

    use_container_width=True

)



# COMPANY RANKING

st.write(
    "## Company Ranking"
)

ranking_df = scores_df.sort_values(

    by="ESG_Score",

    ascending=False

)

st.dataframe(

    ranking_df,

    use_container_width=True

)