from app.database.database import get_connection


def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (

        id TEXT PRIMARY KEY,
        title TEXT,
        company TEXT,
        location TEXT,
        city TEXT,
        country TEXT,
        category TEXT,
        url TEXT,
        description TEXT

    )
    """)

    conn.commit()
    conn.close()


def save_jobs(jobs):

    conn = get_connection()
    cursor = conn.cursor()

    for job in jobs:

        cursor.execute("""
        INSERT OR REPLACE INTO jobs
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            job.id,
            job.title,
            job.company,
            job.location,
            job.city,
            job.country,
            job.category,
            job.url,
            job.description
        ))

    conn.commit()
    conn.close()


def get_all_jobs():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        title,
        company,
        location,
        city,
        country,
        category,
        url,
        description
    FROM jobs
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def count_jobs():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM jobs")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def find_by_city(city):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        title,
        company,
        city
    FROM jobs
    WHERE city = ?
    """, (city,))

    rows = cursor.fetchall()

    conn.close()

    return rows


def find_by_category(category):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        title,
        company,
        category
    FROM jobs
    WHERE category = ?
    """, (category,))

    rows = cursor.fetchall()

    conn.close()

    return rows