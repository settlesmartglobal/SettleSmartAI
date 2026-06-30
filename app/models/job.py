from dataclasses import dataclass


@dataclass
class Job:
    title: str
    company: str
    location: str
    apply_url: str

    def display(self):
        print("=" * 60)
        print("Title    :", self.title)
        print("Company  :", self.company)
        print("Location :", self.location)
        print("Apply    :", self.apply_url)