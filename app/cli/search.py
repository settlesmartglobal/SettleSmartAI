from app.database.job_repository import search_jobs


def search(keyword):

    jobs = search_jobs(keyword)

    print()
    print("=" * 50)
    print("SEARCH RESULTS")
    print("=" * 50)

    print(f"\nKeyword : {keyword}")
    print(f"Results : {len(jobs)}\n")

    if not jobs:
        print("No jobs found.")
        return

    print("-" * 50)

    for title, company, city, category in jobs:

        print(title)
        print(f"Company : {company}")
        print(f"City    : {city}")
        print(f"Category: {category}")
        print("-" * 50)