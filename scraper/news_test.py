import requests

url = "https://www.bbc.com/news"

response = requests.get(url)

print(response.status_code)