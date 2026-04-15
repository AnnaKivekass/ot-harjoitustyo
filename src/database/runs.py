"""db operations for runs"""
from database.connection import db_connection

def add_run(distance, minutes, date):
    """insert run into db"""
    db = db_connection()
    db.execute(
        "INSERT INTO runs (distance, minutes, date) VALUES (?, ?, ?)",
        (distance, minutes, date)
    )
    db.commit()
    db.close()

def get_runs():
    """fetch all runs"""
    db = db_connection()
    rows = db.execute("SELECT * FROM runs").fetchall()
    db.close()
    return rows

def delete_run(run_id):
    """delete a run by id"""
    db = db_connection()
    db.execute("DELETE FROM runs WHERE id = ?", (run_id,))
    db.commit()
    db.close()
