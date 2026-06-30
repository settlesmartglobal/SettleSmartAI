import sqlite3
import os

DATABASE_PATH = "output/jobs.db"


def get_connection():

    os.makedirs("output", exist_ok=True)

    return sqlite3.connect(DATABASE_PATH)