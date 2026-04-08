import unittest
from run import RunApp

from database.connection import init_db
from database.runs import get_runs, delete_run

class TestRunApp(unittest.TestCase):

    def setUp(self):
        init_db()
        self.app = RunApp()

        rows = get_runs()
        for row in rows:
            delete_run(row["id"])

    def test_add_run(self):
        self.app.add_run(10, 60, "26.3.2026")

        runs = self.app.list_runs()
        self.assertEqual(len(runs), 1)

    def test_delete_run(self):
        self.app.add_run(10, 60, "26.3.2026")

        db_runs = get_runs()
        run_id = db_runs[0]["id"]

        result = self.app.delete_run(run_id)
        self.assertTrue(result)

        runs = self.app.list_runs()
        self.assertEqual(len(runs), 0)