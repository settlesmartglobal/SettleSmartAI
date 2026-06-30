import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    APP_ENV = os.getenv("APP_ENV", "development")

    DATABASE_PATH = os.getenv(
        "DATABASE_PATH",
        "output/jobs.db"
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY"
    )


settings = Settings()