from app.ai.resume_parser import ResumeParser
from app.ai.skill_extractor import SkillExtractor
from app.ai.job_matcher import JobMatcher

parser = ResumeParser()
skills = SkillExtractor()
matcher = JobMatcher()

resume = parser.resume_data(
    "resumes/Suresh_Selvam_S.pdf"
)

resume_skills = skills.extract(
    resume["text"]
)

matches = matcher.match_jobs(
    resume_skills
)

print("=" * 60)
print("SETTLESMART AI")
print("TOP MATCHING JOBS")
print("=" * 60)

print()

for job in matches:

    print(f"{job['score']}%")

    print(job["title"])

    print(job["company"])

    print(job["city"])

    print("-" * 40)