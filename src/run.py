class Run:
    def __init__(self, distance, minutes, date):
        self.distance = distance
        self.minutes = minutes
        self.date = date

    def pace(self):
        return self.minutes / self.distance
    
    def speed(self):
        return self.distance / (self.minutes / 60)

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

    def distance_total(self):
        return sum(run.distance for run in self.runs)
    
    def average_pace(self):
        if not self.runs:
            return 0
        
        distance_total= sum(run.distance for run in self.runs)
        minutes_total = sum(run.minutes for run in self.runs)

        return minutes_total / self.distance_total()
    
    def longest_run(self):
        if not self.runs:
            return None
        
        longest = self.runs[0]

        for run in self.runs:
            if run.distance >longest.distance:
                longest = run

        return longest
    
    def average_distance(self):
        if not self.runs:
            return 0
        return self.distance_total() / len(self.runs)
    
    def find_date(self, date):
        return[run for run in self.runs if run.date == date]