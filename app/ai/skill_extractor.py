class SkillExtractor:

    SKILLS = [

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
        "Offboarding",
        "MS Excel",
        "Power BI",
        "Process Improvement",
        "Generative AI",
        "Six Sigma"
    ]

    def extract(self, text):

        found = []

        lower_text = text.lower()

        for skill in self.SKILLS:

            if skill.lower() in lower_text:
                found.append(skill)

        return sorted(found)