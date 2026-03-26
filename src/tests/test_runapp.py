import unittest
from run import RunApp

class TestRunApp(unittest.TestCase):

    def setUp(self):
        self.app = RunApp()

    def test_add_run(self):
        self.app.add_run(10, 60, "26.3.2026")

        runs = self.app.list_runs()
        self.assertEqual(len(runs), 1)
