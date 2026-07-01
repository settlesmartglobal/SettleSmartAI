from app.ai.ats_scorer import ATSScorer
from app.ai.skill_extractor import SkillExtractor
from app.ai.resume_parser import ResumeParser

parser = ResumeParser()
skills = SkillExtractor()
scorer = ATSScorer()

resume = parser.resume_data(
    "resumes/Suresh_Selvam_S.pdf"
)

resume_skills = skills.extract(
    resume["text"]
)

job_skills = [
    "HR Operations",
    "Payroll",
    "Employee Relations",
    "SAP HCM",
    "SuccessFactors",
    "Workday",
    "HR Analytics",
    "Power BI",
    "Leadership",
    "Recruitment"
]

result = scorer.score(
    resume_skills,
    job_skills
)

print("=" * 60)
print("SETTLESMART AI")
print("ATS REPORT")
print("=" * 60)

print()

print("ATS Score:", result["score"], "%")

print()

print("Matched Skills")

for skill in result["matched"]:
    print("✓", skill)

print()

print("Missing Skills")

for skill in result["missing"]:
    print("✗", skill)