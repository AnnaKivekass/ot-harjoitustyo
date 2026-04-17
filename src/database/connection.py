"""Database connection"""

import sqlite3
import os


def db_connection(test=False):
    """create a db connection and return it"""
    base_dir = os.path.dirname(__file__)

    if test:
        db_path = os.path.join(base_dir, "test.db")
    else:
        db_path = os.path.join(base_dir, "runs.db")

    db = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row
    return db


def init_db(test=False):
    """Initialize the db"""
    db = db_connection(test)

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