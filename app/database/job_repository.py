from datetime import datetime
from app.database.database import get_connection


def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        external_id TEXT,

        title TEXT,
        company TEXT,
        location TEXT,
        city TEXT,
        country TEXT,
        category TEXT,

        url TEXT UNIQUE,

        description TEXT,

        created_at TEXT,
        last_seen TEXT,
        is_active INTEGER

    )
    """)

    conn.commit()
    conn.close()


def save_jobs(jobs):

    conn = get_connection()
    cursor = conn.cursor()

    today = datetime.now().isoformat()

    inserted = 0
    skipped = 0

    for job in jobs:

        # Check whether this job already exists
        cursor.execute(
            "SELECT id FROM jobs WHERE url = ?",
            (job.url,)
        )

        existing = cursor.fetchone()

        if existing:
            skipped += 1
            continue

        cursor.execute("""
            INSERT INTO jobs (
                external_id,
                title,
                company,
                location,
                city,
                country,
                category,
                url,
                description,
                created_at,
                last_seen,
                is_active
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            job.external_id,
            job.title,
            job.company,
            job.location,
            job.city,
            job.country,
            job.category,
            job.url,
            job.description,
            today,
            today,
            1
        ))

        inserted += 1

    conn.commit()
    conn.close()

    return inserted, skipped

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
    SELECT title, company, city
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
    SELECT title, company, category
    FROM jobs
    WHERE category = ?
    """, (category,))

    rows = cursor.fetchall()

    conn.close()

    return rows
def search_jobs(keyword):

    conn = get_connection()
    cursor = conn.cursor()

    search = f"%{keyword}%"

    cursor.execute("""
        SELECT title,
               company,
               city,
               category
        FROM jobs
        WHERE
            title LIKE ?
            OR company LIKE ?
            OR city LIKE ?
            OR category LIKE ?
        ORDER BY company, title
    """, (
        search,
        search,
        search,
        search
    ))

    results = cursor.fetchall()

    conn.close()

    return results
def count_companies():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(DISTINCT company)
        FROM jobs
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count
def count_cities():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(DISTINCT city)
        FROM jobs
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count
def count_categories():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(DISTINCT category)
        FROM jobs
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count
def top_companies(limit=10):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT company,
               COUNT(*)
        FROM jobs
        GROUP BY company
        ORDER BY COUNT(*) DESC
        LIMIT ?
    """, (limit,))

    results = cursor.fetchall()

    conn.close()

    return results
def top_categories(limit=10):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category,
               COUNT(*)
        FROM jobs
        GROUP BY category
        ORDER BY COUNT(*) DESC
        LIMIT ?
    """, (limit,))

    results = cursor.fetchall()

    conn.close()

    return results