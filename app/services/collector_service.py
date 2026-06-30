from app.collectors.emirates_api import collect


class CollectorService:

    def collect_all_jobs(self):

        print("\nStarting collectors...\n")

        jobs = []

        emirates_jobs = collect()

        print(f"Emirates: {len(emirates_jobs)} jobs collected")

        jobs.extend(emirates_jobs)

        print(f"\nTotal jobs collected: {len(jobs)}")

        return jobs