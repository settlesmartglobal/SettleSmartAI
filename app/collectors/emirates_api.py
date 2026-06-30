import requests
from app.models.job import Job


def collect():

    jobs = []

    url = "https://www.emiratesgroupcareers.com/api/v1/jobs"

    params = {
        "title": "",
        "brand": "",
        "category": "",
        "location": "",
        "jobcategory": "",
        "showAll": "false"
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    print("=" * 60)
    print("EMIRATES API")
    print("=" * 60)

    print("Status:", data["status"])
    print("Jobs returned:", len(data["data"]))
    print()

    
    for item in data["data"]:

        job = Job(
    id=str(item.get("id", "")),
    title=item.get("title", ""),
    company=item.get("brand", ""),
    location=item.get("location", ""),
    city=item.get("city", ""),
    country=item.get("country", ""),
    category=item.get("category", ""),
    url=item.get("redirectionurl", ""),
    description=item.get("jobdescription", "")
)

        jobs.append(job)

    return jobs