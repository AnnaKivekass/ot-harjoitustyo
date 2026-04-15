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

    def test_distance_total(self):
        self.app.add_run(5, 30, "26.3")
        self.assertEqual(self.app.distance_total(), 5)

    def test_distance_total_two_runs(self):
        self.app.add_run(10, 60, "26.3.2026")
        self.app.add_run(15, 90, "8.4.2026")

        self.assertEqual(self.app.distance_total(), 25)

    def test_distance_total_many_runs(self):
        self.app.add_run(1, 6, "26.3.2026")
        self.app.add_run(5, 30, "13.4.2026")
        self.app.add_run(10, 60, "12.4.2026")
        self.app.add_run(20, 120, "10.4.2026")    

        self.assertEqual(self.app.distance_total(), 36)

    def test_average_pace(self):
        self.app.add_run(10, 60, "26.3.2026")
        self.app.add_run(5, 30, "13.4.2026")

        self.assertEqual(self.app.average_pace(), 6)

    def test_average_pace_no_runs(self):
        self.assertEqual(self.app.average_pace(), 0)

    def test_longest_run(self):
        self.app.add_run(10, 60, "26.3.2026")
        self.app.add_run(5, 30, "13.4.2026")

        longest = self.app.longest_run()
        self.assertEqual(longest.distance, 10)

    def test_fastest_run(self):
        self.app.add_run(10, 60, "26.3.2026")
        self.app.add_run(5, 20, "13.4.2026")

        fastest = self.app.fastest_run()
        self.assertEqual(fastest.distance, 5)             
                    
    def test_search_by_date(self):
        self.app.add_run(10, 60, "26.3.2026")
        self.app.add_run(5, 30, "13.4.2026")
        self.app.add_run(15, 90, "26.3.2026")

        runs = self.app.find_date("26.3.2026")
        self.assertEqual(len(runs), 2)

    def test_average_distance(self):
        self.app.add_run(10, 60, "26.3.2026")
        self.app.add_run(5, 30, "13.4.2026")

        self.assertEqual(self.app.average_distance(), 7.5)
        
    def test_average_distance_no_runs(self):
        self.assertEqual(self.app.average_distance(), 0)
                         

    def test_update_run(self):
        self.app.add_run(10, 60, "26.3.2026")

        db_runs = get_runs()
        run_id = db_runs[0]["id"]

        self.app.update_run(run_id, 15, 90, "8.4.2026")

        runs = self.app.list_runs()
        self.assertEqual(len(runs), 1)
        
    def test_sort_by_date(self):
        self.app.add_run(10, 60, "26.3.2026")
        self.app.add_run(5, 30, "15.4.2026")
        
        sorted_runs = self.app.sort_by_date()
        self.assertEqual(sorted_runs[0].date, "15.4.2026")
        self.assertEqual(sorted_runs[1].date, "26.3.2026")

  
    def test_sort_by_distance(self):
        self.app.add_run(10, 60, "26.3.2026")
        self.app.add_run(5, 30, "15.4.2026")

        sorted_runs = self.app.sort_by_distance()
        self.assertEqual(sorted_runs[0].distance, 10)
        self.assertEqual(sorted_runs[1].distance, 5)