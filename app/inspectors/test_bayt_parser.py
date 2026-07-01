import requests
from bs4 import BeautifulSoup

url = "https://www.bayt.com/en/uae/jobs/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    )
}

print("=" * 60)
print("BAYT HTML TEST")
print("=" * 60)

response = requests.get(url, headers=headers, timeout=30)

print("Status:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("a", attrs={"data-js-id": "jobID"})

print("\nJobs Found:", len(titles))
print("-" * 40)

for job in titles[:10]:
    print(job.get_text(strip=True))