import requests
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"

response = requests.get(url)


if response.status_code == 200:

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    print("=== Page Information ===")

    print("Title:", soup.title.text)


    print("\n=== Quotes ===")

    quotes = soup.find_all(
        "span",
        class_="text"
    )

    authors = soup.find_all(
        "small",
        class_="author"
    )


    for quote, author in zip(quotes, authors):

        print(
            f"{author.text}: {quote.text}"
        )

else:

    print(
        "Failed to fetch webpage:",
        response.status_code
    )