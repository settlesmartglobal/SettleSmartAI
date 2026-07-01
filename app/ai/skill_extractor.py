from app.ai.skill_library import SkillLibrary


class SkillExtractor:

    def __init__(self):

        library = SkillLibrary()

        self.skills = library.get_all_skills()

    def extract(self, text):

        found = []

        text = text.lower()

        for skill in self.skills:

            if skill.lower() in text:
                found.append(skill)

        return sorted(found)