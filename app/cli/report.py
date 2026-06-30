from app.database.job_repository import (
    count_jobs,
    find_by_city,
    find_by_category
)


def report():

    print()
    print("=" * 50)
    print("DATABASE REPORT")
    print("=" * 50)

    print(f"\nTotal Jobs : {count_jobs()}")

    print("\nDubai Jobs")
    print("-" * 40)

    for job in find_by_city("Dubai")[:5]:
        print(job)

    print("\nIT Jobs")
    print("-" * 40)

    for job in find_by_category("Information Technology")[:5]:
        print(job)