"""db connection"""
import sqlite3

def db_connection():
    """create db connection"""
    db = sqlite3.connect("runs.db")
    db.row_factory = sqlite3.Row
    return db

def init_db():
    """initialize the db"""
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

