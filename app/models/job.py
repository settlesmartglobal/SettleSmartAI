from dataclasses import dataclass
from datetime import datetime


@dataclass
class Job:

    title: str
    company: str
    location: str
    source: str
    url: str

    salary: str = ""
    employment_type: str = ""
    posted_date: str = ""
    collected_at: datetime = datetime.now()

    match_score: float = 0

    application_status: str = "Not Applied"

    notes: str = ""