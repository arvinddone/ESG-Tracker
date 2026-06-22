import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="ESG Dashboard")

df = pd.read_csv(
    "data/infosys_esg_sentiment.csv"
)

st.title("ESG Intelligence Dashboard")

st.subheader("Company : Infosys")

st.metric(
    label="Overall ESG Score",
    value="87/100"
)

positive = len(
    df[df["Sentiment"] == "Positive"]
)

neutral = len(
    df[df["Sentiment"] == "Neutral"]
)

negative = len(
    df[df["Sentiment"] == "Negative"]
)

st.write("### Sentiment Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Positive", positive)
col2.metric("Neutral", neutral)
col3.metric("Negative", negative)






sentiment_data = {
    "Sentiment": ["Positive", "Neutral", "Negative"],
    "Count": [positive, neutral, negative]
}

chart_df = pd.DataFrame(sentiment_data)

fig = px.pie(
    chart_df,
    names="Sentiment",
    values="Count",
    title="Sentiment Distribution"
)

st.plotly_chart(fig)


st.write("### ESG Category Distribution")

category_counts = (
    df["ESG_Category"]
    .value_counts()
    .reset_index()
)

category_counts.columns = [
    "Category",
    "Count"
]

st.dataframe(category_counts)








st.write("## ESG Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Overall ESG",
    "87"
)

col2.metric(
    "Articles",
    len(df)
)

col3.metric(
    "Positive News",
    positive
)

col4.metric(
    "Negative News",
    negative
)




category_counts = (
    df["ESG_Category"]
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
    title="ESG Category Distribution"
)

st.plotly_chart(fig2)




st.write("### Recent Articles")
st.dataframe(
    df[
        [
            "Title",
            "ESG_Category",
            "Sentiment"
        ]
    ]
)




company = st.text_input(
    "Enter Company Name",
    "Infosys"
)