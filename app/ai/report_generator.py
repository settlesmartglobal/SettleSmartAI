from app.ai.resume_parser import ResumeParser
from app.ai.skill_extractor import SkillExtractor
from app.ai.ats_scorer import ATSScorer
from app.ai.job_matcher import JobMatcher


class ReportGenerator:

    def __init__(self):

        self.parser = ResumeParser()
        self.skills = SkillExtractor()
        self.matcher = JobMatcher()
        self.scorer = ATSScorer()

    def generate(self, resume_path):

        resume = self.parser.resume_data(resume_path)

        resume_skills = self.skills.extract(
            resume["text"]
        )

        matches = self.matcher.match_jobs(
            resume_skills
        )

        report = {

            "name": resume["name"],
            "email": resume["email"],
            "phone": resume["phone"],

            "skills": resume_skills,

            "top_jobs": matches

        }

        return report