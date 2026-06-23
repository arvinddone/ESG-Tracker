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

scores_df = pd.read_csv(
    "data/company_esg_scores.csv"
)

articles_df = pd.read_csv(
    "data/all_esg_sentiment.csv"
)


# TITLE

st.markdown("""
#  ESG Intelligence Platform

### AI Powered ESG Risk & Sentiment Analysis

Track ESG performance using:
- News Scraping
- ESG Classification
- Sentiment Analysis
- ESG Scoring Engine
""")


# SIDEBAR

st.sidebar.title("📌 Project Workflow")

st.sidebar.info("""
Company

⬇

News Scraping

⬇

Article Extraction

⬇

ESG Classification

⬇

Sentiment Analysis

⬇

ESG Score

⬇

Dashboard
""")

st.sidebar.markdown("---")

st.sidebar.subheader("ESG Meaning")

st.sidebar.success("E = Environmental")
st.sidebar.warning("S = Social")
st.sidebar.error("G = Governance")


# COMPANY SELECTOR

selected_company = st.selectbox(
    "Select Company",
    scores_df["Company"]
)


# COMPANY DATA

company_score = scores_df[
    scores_df["Company"] == selected_company
]

score = company_score[
    "ESG_Score"
].values[0]


# FILTER ARTICLES

company_articles = articles_df[
    articles_df["Company"] == selected_company
]


# RISK LEVEL

if score >= 90:
    risk = "🟢 Low Risk"

elif score >= 75:
    risk = "🟡 Medium Risk"

else:
    risk = "🔴 High Risk"


# ESG OVERVIEW

st.write("## 🌍 ESG Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "ESG Score",
    round(score, 2)
)

col2.metric(
    "Risk Level",
    risk
)

col3.metric(
    "ESG Articles",
    len(company_articles)
)


# SENTIMENT COUNTS

positive = len(
    company_articles[
        company_articles["Sentiment"] == "Positive"
    ]
)

neutral = len(
    company_articles[
        company_articles["Sentiment"] == "Neutral"
    ]
)

negative = len(
    company_articles[
        company_articles["Sentiment"] == "Negative"
    ]
)


# SENTIMENT SUMMARY

st.write("##  Sentiment Summary")

c1, c2, c3 = st.columns(3)

c1.metric("Positive", positive)
c2.metric("Neutral", neutral)
c3.metric("Negative", negative)


# COMPANY INFO BOX

st.success(
    f"""
Selected Company: {selected_company}

ESG Score: {round(score,2)}

Risk Level: {risk}

Positive News: {positive}

Negative News: {negative}
"""
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
    width="stretch"
)


# ESG CATEGORY DISTRIBUTION

st.write(
    "## 📊 ESG Category Distribution"
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
    width="stretch"
)


# RECENT ARTICLES

st.write("## 📰 Latest ESG Articles")

latest_articles = company_articles.tail(10)

st.dataframe(
    latest_articles[
        [
            "Title",
            "ESG_Category",
            "Sentiment"
        ]
    ],
    width="stretch"
)


# COMPANY RANKING

st.write("## 🏆 ESG Leaderboard")

ranking_df = scores_df.sort_values(
    by="ESG_Score",
    ascending=False
)

st.dataframe(
    ranking_df,
    width="stretch"
)

st.write("### Top Ranked Companies")

for idx, row in ranking_df.head(5).iterrows():

    rank = ranking_df.index.get_loc(idx) + 1

    if rank == 1:
        medal = "🥇"

    elif rank == 2:
        medal = "🥈"

    elif rank == 3:
        medal = "🥉"

    else:
        medal = f"{rank}️⃣"

    st.write(
        f"{medal} {row['Company']} | ESG Score: {row['ESG_Score']}"
    )

# FOOTER

st.markdown("---")

st.caption("""
Built by Arvind Done

B.Tech Computer Engineering

Python | NLP | ESG Analytics | Streamlit
""")