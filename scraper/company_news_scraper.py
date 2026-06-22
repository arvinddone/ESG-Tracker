import pandas as pd

companies = pd.read_csv(
    "data/companies.csv"
)

print("Total Companies:",
      len(companies))

for company in companies["Company"]:

    print(company)

