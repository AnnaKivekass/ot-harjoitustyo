import tkinter as tk
from tkinter import messagebox

from run import RunApp
from database.connection import init_db
from database.runs import get_runs

class RunGUI:
    def __init__(self, root):
        self.app = RunApp()
        self.editing_id = None
        self.runs = []

        root.title("Run App")

        tk.Label(root, text="Distance (km)").grid(row=0, column=0)
        self.distance_entry = tk.Entry(root)
        self.distance_entry.grid(row=0, column=1)

        tk.Label(root, text="Minutes").grid(row=1, column=0)
        self.minutes_entry = tk.Entry(root)
        self.minutes_entry.grid(row=1, column=1)

        tk.Label(root, text="Date").grid(row=2, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=2, column=1)

        tk.Button(root, text="Add Run", command=self.add_run).grid(row=3, column=0)
        tk.Button(root, text="Delete Selected", command=self.delete_run).grid(row=3, column=1)
        tk.Button(root, text="Load Selected", command=self.load_selected).grid(row=3, column=2)

        tk.Button(root, text="Total Distance", command=self.total_distance).grid(row=4, column=0)
        tk.Button(root, text="Average Pace", command=self.average_pace).grid(row=4, column=1)

        tk.Button(root, text="Longest Run", command=self.longest_run).grid(row=5, column=0)
        tk.Button(root, text="Average Distance", command=self.average_distance).grid(row=5, column=1)
        tk.Button(root, text="Fastest Run", command=self.fastest_run).grid(row=5, column=2)

        tk.Button(root, text="Search by Date", command=self.search_by_date).grid(row=6, column=0, columnspan=2)
        tk.Button(root, text="Show All", command=self.refresh_list).grid(row=6, column=2)

        self.listbox = tk.Listbox(root, width=60)
        self.listbox.grid(row=7, column=0, columnspan=3)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=8, column=0, columnspan=3)

        self.refresh_list()

    def add_run(self):
        try:
            distance = float(self.distance_entry.get())
            minutes = float(self.minutes_entry.get())
            date = self.date_entry.get()

            if self.editing_id:
                self.app.delete_run(self.editing_id)
                self.app.add_run(distance, minutes, date)
                self.editing_id = None
            else:
                self.app.add_run(distance, minutes, date)

            self.refresh_list()
            self.clear_fields()

        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def delete_run(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Select a run first")
            return

        index = selection[0]
        run_id = self.runs[index]["id"]

        self.app.delete_run(run_id)
        self.refresh_list()

    def load_selected(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Select a run first")
            return

        index = selection[0]
        run = self.runs[index]

        self.editing_id = run["id"]

        self.distance_entry.delete(0, tk.END)
        self.distance_entry.insert(0, run["distance"])

        self.minutes_entry.delete(0, tk.END)
        self.minutes_entry.insert(0, run["minutes"])

        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, run["date"])

    def total_distance(self):
        total = self.app.distance_total()
        self.result_label.config(text=f"Total distance: {total} km")

    def average_pace(self):
        pace = self.app.average_pace()
        self.result_label.config(text=f"Average pace: {round(pace, 2)} min/km")

    def longest_run(self):
        run = self.app.longest_run()
        if run:
            self.result_label.config(text=f"Longest run: {run.distance} km on {run.date}")
        else:
            self.result_label.config(text="No runs found")

    def average_distance(self):
        avg = self.app.average_distance()
        self.result_label.config(text=f"Average distance: {round(avg, 2)} km")

    def search_by_date(self):
        date = self.date_entry.get()
        runs = self.app.find_date(date)

        self.listbox.delete(0, tk.END)
        self.runs = runs

        for run in runs:
            text = f"{run.distance} km, {run.minutes} min, {run.date}"
            self.listbox.insert(tk.END, text)

    def refresh_list(self):
        self.listbox.delete(0, tk.END)

        self.runs = get_runs()

        for run in self.runs:
            text = (
                f"{run['distance']} km, {run['minutes']} min, {run['date']}"
            )
            self.listbox.insert(tk.END, text)

    def fastest_run(self):
        run = self.app.fastest_run()
        if run:
            self.result_label.config(
                text=f"Fastest run: {run.distance} km, {run.minutes} min, {run.date}, pace {round(run.pace(), 2)} min/km"
            )
        else:
            self.result_label.config(text="No runs found")

    def clear_fields(self):
        self.distance_entry.delete(0, tk.END)
        self.minutes_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)


def main():
    init_db()
    root = tk.Tk()
    RunGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()