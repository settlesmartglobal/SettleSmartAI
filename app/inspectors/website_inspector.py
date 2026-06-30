from bs4 import BeautifulSoup
from app.utils.http_client import get


def inspect(url):

    response = get(url)

    soup = BeautifulSoup(response.text, "lxml")

    print("=" * 60)
    print("Website Inspector")
    print("=" * 60)

    print("Title :", soup.title.text)

    print()

    print("Number of Links :", len(soup.find_all("a")))

    print("Number of Scripts :", len(soup.find_all("script")))

    print("Forms :", len(soup.find_all("form")))
    