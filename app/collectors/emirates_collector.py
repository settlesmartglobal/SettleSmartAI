from app.utils.http_client import get
from app.parser.html_parser import parse


def collect():

    url = "https://www.emiratesgroupcareers.com"

    html = get(url)

    soup = parse(html)

    print("=" * 60)
    print("Emirates Careers Collector")
    print("=" * 60)

    print("Website Title :", soup.title.text)

    print()

    links = soup.find_all("a")

    print("Total Links Found :", len(links))

    print()

    for link in links[:20]:

        text = link.get_text(strip=True)

        href = link.get("href")

        if text:

            print(text)

            print(href)

            print("-" * 40)