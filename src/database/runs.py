from database.connection import db_connection


def add_run(distance, minutes, date):
    db = db_connection()
    db.execute(
        "INSERT INTO runs (distance, minutes, date) VALUES (?, ?, ?)",
        (distance, minutes, date)
    )
    db.commit()
    db.close()


def get_runs():
    db = db_connection()
    rows = db.execute("SELECT * FROM runs").fetchall()
    db.close()
    return rows


def delete_run(run_id):
    db = db_connection()
    db.execute("DELETE FROM runs WHERE id = ?", (run_id,))
    db.commit()
    db.close()