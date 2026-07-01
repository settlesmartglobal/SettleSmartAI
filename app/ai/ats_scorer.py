class ATSScorer:

   def score(self, resume_skills, job_skills):

    if not job_skills:

        return {
            "score": 0,
            "matched": [],
            "missing": []
        }

    matched = []

    for skill in job_skills:

        if skill in resume_skills:
            matched.append(skill)

    score = round(
        (len(matched) / len(job_skills)) * 100
    )

    return {

        "score": score,

        "matched": matched,

        "missing": [

            skill
            for skill in job_skills
            if skill not in resume_skills

        ]

    }