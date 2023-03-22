import requests
from bs4 import BeautifulSoup

search_url = "https://www.google.com/search"
search_term = "hotels.cloudbeds.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

response = requests.get(search_url, headers=headers, params={"q": search_term})
soup = BeautifulSoup(response.text, "html.parser")

results = []
for g in soup.find_all('div', class_='g'):
    a = g.find('a')
    if a:
        url = a['href']
        if "hotels.cloudbeds.com" in url:
            results.append(url)

print(results)
