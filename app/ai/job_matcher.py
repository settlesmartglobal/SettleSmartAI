from app.database.job_repository import get_all_jobs
from app.ai.ats_scorer import ATSScorer


class JobMatcher:

    def __init__(self):
        self.scorer = ATSScorer()

    def extract_job_skills(self, description):

        skills = [
            "HR Operations",
            "HR Shared Services",
            "HR Business Partner",
            "Recruitment",
            "Payroll",
            "Compliance",
            "MOHRE",
            "WPS",
            "Emiratisation",
            "SAP HCM",
            "SuccessFactors",
            "Workday",
            "Zoho People",
            "HR Analytics",
            "Employee Relations",
            "Vendor Management",
            "Training",
            "Onboarding",
            "Power BI",
            "MS Excel",
            "Leadership",
            "Process Improvement",
            "Generative AI"
        ]

        if not description:
            return []

        text = description.lower()

        found = []

        for skill in skills:
            if skill.lower() in text:
                found.append(skill)

        return found

    def match_jobs(self, resume_skills):

        matches = []

        jobs = get_all_jobs()

        for job in jobs:

            description = job[9]

            job_skills = self.extract_job_skills(description)

            if not job_skills:
                continue

            result = self.scorer.score(
                resume_skills,
                job_skills
            )

            matches.append({
                "title": job[2],
                "company": job[3],
                "city": job[5],
                "score": result["score"]
            })

        matches.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return matches[:10]