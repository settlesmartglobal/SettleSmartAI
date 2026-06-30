from app.database.job_repository import (
    count_jobs,
    count_companies,
    count_cities,
    count_categories,
    top_companies,
    top_categories
)


def stats():

    print()
    print("=" * 50)
    print("DATABASE STATISTICS")
    print("=" * 50)

    print()

    print(f"Total Jobs      : {count_jobs()}")
    print(f"Companies       : {count_companies()}")
    print(f"Cities          : {count_cities()}")
    print(f"Categories      : {count_categories()}")

    print()

    print("Top Companies")
    print("-" * 40)

    for company, total in top_companies():
        print(f"{company:<30} {total}")

    print()

    print("Top Categories")
    print("-" * 40)

    for category, total in top_categories():
        print(f"{category:<30} {total}")