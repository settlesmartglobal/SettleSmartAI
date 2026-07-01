from app.collectors.emirates_api import collect as collect_emirates

COLLECTORS = [
    ("Emirates", collect_emirates),
]