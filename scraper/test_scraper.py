import requests

url = "https://example.com"

response = requests.get(url)

print(response.status_code)


import requests
from bs4 import BeautifulSoup

url = "https://www.moneycontrol.com/news/tags/infosys-ltd.html"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print("Title:")
print(soup.title.text)