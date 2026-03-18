import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://quotes.toscrape.com"

quotes = []
authors = []
tags_list = []

page_number = 1

while True:
    url = f"{base_url}/page/{page_number}/"
    response = requests.get(url)

    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, "html.parser")
    quote_blocks = soup.find_all("div", class_="quote")

    if not quote_blocks:
        break

    for quote in quote_blocks:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]

        quotes.append(text)
        authors.append(author)
        tags_list.append(", ".join(tags))

    print(f"Page {page_number} scraped")
    page_number += 1

df = pd.DataFrame({"Quote": quotes, "Author": authors, "Tags": tags_list})

df.to_csv("quotes_all_pages.csv", index=False, encoding="utf-8")

print(" All pages scraped! File saved as quotes_all_pages.csv")
