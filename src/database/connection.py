"""Database connection"""

import sqlite3
import os


def db_connection():
    """Create and return database connection"""
    base_dir = os.path.dirname(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, "runs.db")

    db = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row
    return db


def init_db():
    """Initialize the db"""
    db = db_connection()
    db.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY,
            distance REAL,
            minutes INTEGER,
            date TEXT
        )
    """)
    db.commit()
    db.close() 
