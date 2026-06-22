import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

df = pd.read_csv(
    "data/all_headlines_with_links.csv"
)

all_articles = []

for index, row in df.iterrows():

    company = row["Company"]
    title = row["Headline"]
    link = row["Link"]

    print(
        f"Processing {index+1}/{len(df)}"
    )

    try:

        response = requests.get(
            link,
            headers={
                "User-Agent":
                "Mozilla/5.0"
            },
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        article_content = soup.find(
            "div",
            class_="content_wrapper"
        )

        if article_content:

            article_text = (
                article_content.get_text(
                    separator=" ",
                    strip=True
                )
            )

        else:

            article_text = (
                "Article Not Found"
            )

        all_articles.append({

            "Company": company,

            "Title": title,

            "Link": link,

            "Article": article_text

        })

        time.sleep(1)

    except Exception as e:

        all_articles.append({

            "Company": company,

            "Title": title,

            "Link": link,

            "Article": f"ERROR: {e}"

        })

result_df = pd.DataFrame(
    all_articles
)

result_df.to_csv(
    "data/all_articles.csv",
    index=False
)

print(
    "\nAll Articles Saved!"
)

print(
    "Total Articles:",
    len(result_df)
)