"""SQLite connection and schema initialization."""
import sqlite3
from contextlib import contextmanager
from .config import DB_PATH

SCHEMA = """
CREATE TABLE IF NOT EXISTS profile (
 id INTEGER PRIMARY KEY CHECK(id=1), name TEXT NOT NULL, target_role TEXT NOT NULL,
 experience_level TEXT NOT NULL, location TEXT NOT NULL, resume_text TEXT NOT NULL,
 skills_json TEXT NOT NULL, updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS roadmap (
 id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, category TEXT NOT NULL,
 description TEXT NOT NULL, skill TEXT NOT NULL, duration TEXT NOT NULL,
 status TEXT NOT NULL DEFAULT 'todo', sort_order INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS applications (
 id INTEGER PRIMARY KEY AUTOINCREMENT, company TEXT NOT NULL, role TEXT NOT NULL,
 location TEXT NOT NULL, stage TEXT NOT NULL, url TEXT NOT NULL,
 follow_up_date TEXT NOT NULL, notes TEXT NOT NULL,
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""

@contextmanager
def connection():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    try:
        yield db
        db.commit()
    finally:
        db.close()

def initialize():
    with connection() as db:
        db.executescript(SCHEMA)
