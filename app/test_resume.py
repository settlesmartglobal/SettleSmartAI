from app.ai.resume_parser import ResumeParser
from app.ai.skill_extractor import SkillExtractor

parser = ResumeParser()
skills = SkillExtractor()

resume = parser.resume_data(
    "resumes/Suresh_Selvam_S.pdf"
)

skill_list = skills.extract(
    resume["text"]
)

print("=" * 60)
print("SETTLESMART AI")
print("Career Intelligence Report")
print("=" * 60)

print()

print("Name")
print(resume["name"])

print()

print("Email")
print(resume["email"])

print()

print("Phone")
print(resume["phone"])

print()

print("=" * 60)
print("Skills Found")
print("=" * 60)

for skill in skill_list:
    print("✓", skill)