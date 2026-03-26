import unittest
from run import RunApp

class TestRunApp(unittest.TestCase):

    def setUp(self):
        self.app = RunApp()

    def test_add_run(self):
        self.app.add_run(10, 60, "26.3.2026")

        runs = self.app.list_runs()
        self.assertEqual(len(runs), 1)

    def test_delete_run(self):
        self.app.add_run(10, 60, "26.3.2026")

        result = self.app.delete_run(0)
        self.assertTrue(result)
        self.assertEqual(len(self.app.runs), 0)