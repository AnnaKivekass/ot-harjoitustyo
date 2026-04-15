"""Database connection"""

import sqlite3
import os

def db_connection():
    db = sqlite3.connect("runs.db")
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
