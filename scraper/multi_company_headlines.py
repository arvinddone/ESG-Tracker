import pandas as pd
import requests
from bs4 import BeautifulSoup

companies = pd.read_csv("data/company_urls.csv")

all_headlines = []

headers = {
    "User-Agent": "Mozilla/5.0"
}

for _, row in companies.iterrows():

    company = row["Company"]
    url = row["URL"]

    print(f"\nProcessing {company}...")

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        headlines = soup.find_all("h2")

        count = 0

        for headline in headlines:

            title = headline.get_text(strip=True)

            parent_a = headline.find_parent("a")

            link = ""

            if parent_a:
                link = parent_a.get("href", "")

            if title:

                all_headlines.append({
                    "Company": company,
                    "Headline": title,
                    "Link": link
                })

                count += 1

        print(f"Found {count} headlines")

    except Exception as e:

        print(f"Error for {company}: {e}")

df = pd.DataFrame(all_headlines)

df.to_csv(
    "data/all_headlines_with_links.csv",
    index=False
)

print("\nDone!")
print("Total Headlines:", len(df))