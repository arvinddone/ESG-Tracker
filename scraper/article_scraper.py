import requests
from bs4 import BeautifulSoup
url = "https://www.moneycontrol.com/news/business/stocks/infosys-stock-falls-over-3-after-q4-top-nifty-loser-weak-guidance-mixed-brokerage-views-weigh-13898182.html"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Failed to fetch article")
    exit()
soup = BeautifulSoup(response.text, "html.parser")

# Title
title = soup.title.text.strip()
# Article Content
article_content = soup.find("div", class_="content_wrapper")
if article_content:
    article_text = article_content.get_text(
        separator="\n",
        strip=True
    )
    print("\nTITLE:\n")
    print(title)
    print("\nARTICLE:\n")
    print(article_text[:3000])
else:
    print("Article content not found")

import pandas as pd
article_data = {
    "Company": ["Infosys"],
    "Title": [title],
    "Link": [url],
    "Article": [article_text]
}
df = pd.DataFrame(article_data)
df.to_csv(
    "data/infosys_articles.csv",
    index=False
)
print("\nArticle CSV Saved Successfully!")