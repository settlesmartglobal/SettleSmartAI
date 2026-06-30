from app.database.job_repository import (
    create_table,
    save_jobs,
    count_jobs,
    find_by_city,
    find_by_category
)
from app.collectors.emirates_api import collect
from app.exporters.csv_exporter import export_jobs


def main():

    print("=" * 60)
    print("🚀 SettleSmart AI")
    print("Sprint 4 - Emirates API Collector")
    print("=" * 60)

    create_table()

    jobs = collect()

    save_jobs(jobs)

    print(f"Saved {len(jobs)} jobs into SQLite database.")

    print(f"\nCollected {len(jobs)} jobs successfully.\n")

    export_jobs(
        jobs,
        "emirates_jobs.csv"
    )
print("=" * 60)

print("DATABASE TEST")

print("=" * 60)

print()

print("Total Jobs :", count_jobs())

print()

print("Dubai Jobs")

print("-" * 40)

for job in find_by_city("Dubai")[:5]:

    print(job)

print()

print("IT Jobs")

print("-" * 40)

for job in find_by_category("Information Technology")[:5]:

    print(job)

if __name__ == "__main__":
    main()