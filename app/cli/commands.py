from app.services.collector_service import CollectorService
from app.database.job_repository import (
    create_table,
    save_jobs,
    count_jobs
)
from app.exporters.csv_exporter import export_jobs


def collect_emirates():

    create_table()

    service = CollectorService()

    jobs = service.collect_all_jobs()

    inserted, skipped = save_jobs(jobs)

    export_jobs(
        jobs,
        "emirates_jobs.csv"
    )

    print()

    print("=" * 40)
    print("Collection Summary")
    print("=" * 40)

    print(f"Downloaded : {len(jobs)}")
    print(f"Inserted   : {inserted}")
    print(f"Skipped    : {skipped}")

    print()

    print(f"Database Total : {count_jobs()}")