from app.ai.report_generator import ReportGenerator


def career_report(resume_path):

    generator = ReportGenerator()

    report = generator.generate(
        resume_path
    )

    print()
    print("=" * 60)
    print("SETTLESMART AI")
    print("Career Intelligence Report")
    print("=" * 60)

    print()

    print("Candidate")
    print("-" * 40)

    print("Name :", report["name"])
    print("Email:", report["email"])
    print("Phone:", report["phone"])

    print()

    print("Skills Found :", len(report["skills"]))

    print()

    for skill in report["skills"]:
        print("✓", skill)

    print()

    print("=" * 60)
    print("Top Matching Jobs")
    print("=" * 60)

    for index, job in enumerate(report["top_jobs"], start=1):

        print()

        print(f"{index}. {job['title']}")

        print("Company :", job["company"])
        print("City    :", job["city"])
        print("Match   :", f"{job['score']}%")