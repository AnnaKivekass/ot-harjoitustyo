"""db operations for runs"""
from database.connection import db_connection


def add_run(distance, minutes, date, test=False):
    """insert run into db"""
    db = db_connection(test)
    db.execute(
        "INSERT INTO runs (distance, minutes, date) VALUES (?, ?, ?)",
        (distance, minutes, date)
    )
    db.commit()
    db.close()


def get_runs(test=False):
    """fetch all runs"""
    db = db_connection(test)
    rows = db.execute("SELECT * FROM runs").fetchall()
    db.close()
    return rows


def delete_run(run_id, test=False):
    """delete a run by id"""
    db = db_connection(test)
    db.execute("DELETE FROM runs WHERE id = ?", (run_id,))
    db.commit()
    db.close()


def update_run(run_id, distance, minutes, date, test=False):
    """update run by id"""
    db = db_connection(test)
    db.execute(
        "UPDATE runs SET distance = ?, minutes = ?, date = ? WHERE id = ?",
        (distance, minutes, date, run_id)
    )
    db.commit()
    db.close()
