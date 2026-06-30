import csv
import os


def export_jobs(jobs, filename):

    os.makedirs("output", exist_ok=True)

    filepath = os.path.join("output", filename)

    with open(filepath, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Title",
            "Company",
            "Location",
            "City",
            "Country",
            "Category",
            "URL"
        ])

        for job in jobs:

            writer.writerow([
                job.id,
                job.title,
                job.company,
                job.location,
                job.city,
                job.country,
                job.category,
                job.url
            ])

    print(f"\nCSV saved to {filepath}")