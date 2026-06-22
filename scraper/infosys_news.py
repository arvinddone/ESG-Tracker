import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.moneycontrol.com/news/tags/infosys-ltd.html"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("h2")

news_data = []

for headline in headlines:

    title = headline.get_text(strip=True)

    parent_a = headline.find_parent("a")

    link = ""

    if parent_a:
        link = parent_a.get("href")

    news_data.append({
        "Company": "Infosys",
        "Headline": title,
        "Link": link
    })

df = pd.DataFrame(news_data)

print(df.head())

df.to_csv(
    "data/infosys_headlines_with_links.csv",
    index=False
)

print("Headline + Link CSV Saved!")

print(df.head())

df.to_csv("data/infosys_headlines_clean.csv", index=False)

print("CSV Saved Successfully!")

print("\nFirst H2 Tag:\n")
print(headlines[0])

print("\nParent Tag:\n")
print(headlines[0].parent)