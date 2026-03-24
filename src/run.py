class Run:
    def __init__(self, distance, minutes, date):
        self.distance = distance
        self.minutes = minutes
        self.date = date

    def pace(self):
        return self.minutes / self.distance


class RunApp:
    def __init__(self):
        self.runs = []

    def add_run(self, distance, minutes, date):
        run = Run(distance, minutes, date)
        self.runs.append(run)

    def list_runs(self):
        return self.runs

    def delete_run(self, index):
        if 0 <= index < len(self.runs):
            self.runs.pop(index)
            return True
        return False

