import requests
from bs4 import BeautifulSoup


def inspect():

    url = "https://www.naukrigulf.com/jobs"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=30
    )

    print("=" * 60)
    print("NAUKRIGULF INSPECTOR")
    print("=" * 60)

    print("Status :", response.status_code)

    soup = BeautifulSoup(response.text, "lxml")

    print("Title :", soup.title.text.strip())

    print("Links :", len(soup.find_all("a")))
    print("Scripts :", len(soup.find_all("script")))
    print("Forms :", len(soup.find_all("form")))