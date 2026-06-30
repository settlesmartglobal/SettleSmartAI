from app.inspectors.website_inspector import inspect


def main():

    print("=" * 60)
    print("SettleSmart AI")
    print("Website Inspector")
    print("=" * 60)

    inspect("https://www.emiratesgroupcareers.com")


if __name__ == "__main__":
    main()