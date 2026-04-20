"""app logic for runs"""
from database.runs import add_run, get_runs, delete_run, update_run


class Run:
    """a single run"""
    def __init__(self, run_id, distance, minutes, date):
        self.id = run_id
        self.distance = distance
        self.minutes = minutes
        self.date = date

    def pace(self):
        """return pace in minutes / km"""
        if self.distance == 0:
            return 0
        return self.minutes / self.distance

    def speed(self):
        """return speed in km/hour"""
        if self.minutes == 0:
            return 0
        return self.distance / (self.minutes / 60)


class RunApp:
    """app logic for handling runs"""

    def __init__(self, test=False):
        self.test = test

    def add_run(self, distance, minutes, date):
        """add a run"""
        add_run(distance, minutes, date, self.test)

    def list_runs(self):
        """return all runs"""
        rows = get_runs(self.test)
        return [
            Run(row["id"], row["distance"], row["minutes"], row["date"])
            for row in rows
        ]

    def delete_run(self, run_id):
        """delete run by id"""
        delete_run(run_id, self.test)
        return True

    def update_run(self, run_id, distance, minutes, date):
        """update existing run"""
        update_run(run_id, distance, minutes, date, self.test)

    def distance_total(self):
        """return total distance"""
        runs_list = self.list_runs()
        return sum(run.distance for run in runs_list)

    def average_pace(self):
        """return average pace in all runs"""
        runs_list = self.list_runs()
        if not runs_list:
            return 0

        distance_total = sum(run.distance for run in runs_list)
        minutes_total = sum(run.minutes for run in runs_list)

        if distance_total == 0:
            return 0

        return minutes_total / distance_total

    def longest_run(self):
        """return longest run in distance"""
        runs_list = self.list_runs()
        if not runs_list:
            return None

        return max(runs_list, key=lambda run: run.distance)

    def fastest_run(self):
        """return run with fastest pace"""
        runs_list = self.list_runs()
        if not runs_list:
            return None

        return min(runs_list, key=lambda run: run.pace())

    def average_distance(self):
        """return average distance"""
        runs_list = self.list_runs()
        if not runs_list:
            return 0
        return self.distance_total() / len(runs_list)

    def find_date(self, date):
        """find runs by date"""
        runs_list = self.list_runs()
        return [run for run in runs_list if run.date == date]

    def sort_by_distance(self):
        """sort runs by longest distance first"""
        runs = self.list_runs()
        return sorted(runs, key=lambda run: run.distance, reverse=True)

    def sort_by_date(self):
        """sort runs by date, oldest first"""
        runs = self.list_runs()
        return sorted(
            runs,
            key=lambda run: tuple(map(int, run.date.split(".")))[::-1]
        )
 
