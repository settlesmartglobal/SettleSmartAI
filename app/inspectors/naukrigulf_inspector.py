import requests
from bs4 import BeautifulSoup


def inspect():

    print("Starting inspector...")

    url = "https://www.naukrigulf.com/jobs"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    print("Sending request...")

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    print("Response received")

    print("Status Code:", response.status_code)
    print("Content Type:", response.headers.get("Content-Type"))

    soup = BeautifulSoup(response.text, "html.parser")

    print("Title:", soup.title.text if soup.title else "No title")
    print("Links:", len(soup.find_all("a")))
    print("Scripts:", len(soup.find_all("script")))


if __name__ == "__main__":
    inspect()