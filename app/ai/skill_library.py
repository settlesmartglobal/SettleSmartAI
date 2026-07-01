import json
from pathlib import Path


class SkillLibrary:

    def __init__(self):

        project_root = Path(__file__).resolve().parents[2]

        self.skills_file = project_root / "data" / "skills.json"

        self.skills = self.load()

    def load(self):

        with open(self.skills_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_categories(self):

        return list(self.skills.keys())

    def get_all_skills(self):

        all_skills = []

        for category in self.skills.values():
            all_skills.extend(category)

        return sorted(set(all_skills))