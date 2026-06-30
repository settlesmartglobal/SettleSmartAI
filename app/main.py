import sys

from app.cli.commands import collect_emirates
from app.cli.report import report
from app.cli.help import help_command
from app.cli.stats import stats
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


def main():

    if len(sys.argv) < 2:
        help_command()
        return

    command = sys.argv[1]

    if command == "collect":

        if len(sys.argv) < 3:
            print("Specify a collector.")
            return

        collector = sys.argv[2]

        if collector == "emirates":
            collect_emirates()
        else:
            print("Unknown collector.")

    elif command == "report":

        report()

    elif command == "search":

        if len(sys.argv) < 3:
            print("Usage: python3 -m app.main search <keyword>")
            return

        keyword = " ".join(sys.argv[2:])

        search(keyword)

    elif command == "stats":

        stats()

    elif command == "help":

        help_command()

    else:

        print("Unknown command.")
        help_command()


if __name__ == "__main__":
    main()