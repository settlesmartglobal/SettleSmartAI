from app.collectors.registry import COLLECTORS


class CollectorService:

    def collect_all_jobs(self):

        print("\nStarting collectors...\n")

        jobs = []

        for name, collector in COLLECTORS:

            collected = collector()

            print(f"{name}: {len(collected)} jobs collected")

            jobs.extend(collected)

        print(f"\nTotal jobs collected: {len(jobs)}")

        return jobs