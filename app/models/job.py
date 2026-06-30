from dataclasses import dataclass


@dataclass
class Job:
    external_id: str
    title: str
    company: str
    location: str
    city: str
    country: str
    category: str
    url: str
    description: str