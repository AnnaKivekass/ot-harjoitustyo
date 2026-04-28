import tkinter as tk

from tkinter import messagebox
from datetime import datetime

from run import RunApp
from database.connection import init_db

from graphs import (
    show_distance_graph,
    show_selected_pace_graph,
    show_graph_with_highlight
)

class RunGUI:
    """GUI app for tracking runs"""
    def __init__(self, root):
        self.app = RunApp()
        self.editing_id = None
        self.runs = []

        root.title("Run App")
        root.configure(bg="#ffe6f0")

        tk.Label(root, text="Run Tracker", font=("Arial", 14)).grid(row=0, column=0, columnspan=4, pady=5)

        tk.Label(root, text="Distance (km)").grid(row=1, column=0, padx=5, pady=5)
        self.distance_entry = tk.Entry(root)
        self.distance_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Minutes").grid(row=2, column=0, padx=5, pady=5)
        self.minutes_entry = tk.Entry(root)
        self.minutes_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(root, text="Date").grid(row=3, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Add Run", command=self.add_run)
        self.add_button.grid(row=4, column=0, padx=5, pady=5)
        tk.Button(root, text="Delete Selected", command=self.delete_run).grid(row=4, column=1, padx=5, pady=5)
        tk.Button(root, text="Load Selected", command=self.load_selected).grid(row=4, column=2, padx=5, pady=5)

        tk.Button(root, text="Total Distance", command=self.total_distance).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(root, text="Average Pace", command=self.average_pace).grid(row=5, column=1, padx=5, pady=5)

        tk.Button(root, text="Longest Run", command=self.longest_run).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(root, text="Average Distance", command=self.average_distance).grid(row=6, column=1, padx=5, pady=5)
        tk.Button(root, text="Fastest Run", command=self.fastest_run).grid(row=6, column=2, padx=5, pady=5)

        tk.Button(root, text="Sort by Distance", command=self.sort_by_distance).grid(row=7, column=0, padx=5, pady=5)
        tk.Button(root, text="Sort by Date", command=self.sort_by_date).grid(row=7, column=1, padx=5, pady=5)
        tk.Button(root, text="Search by Date", command=self.search_by_date).grid(row=7, column=2, padx=5, pady=5)
        tk.Button(root, text="Show All", command=self.refresh_list).grid(row=7, column=3, padx=5, pady=5)

        tk.Button(root, text="Show Graph", command=self.show_graph).grid(row=9, column=0, padx=5, pady=5)
        tk.Button(root, text="Selected Pace", command=self.show_selected_pace).grid(row=9, column=1, padx=5, pady=5)
        tk.Button(root, text="Graph + Highlight", command=self.show_graph_with_selected).grid(row=9, column=2, padx=5, pady=5)

        self.listbox = tk.Listbox(root, width=60)
        self.listbox.grid(row=8, column=0, columnspan=4, padx=5, pady=5)
        self.listbox.bind("<Double-Button-1>", self.show_details)

        scrollbar = tk.Scrollbar(root)
        scrollbar.grid(row=8, column=4, sticky="ns")

        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        self.result_label = tk.Label(root, text="", bg ="#ffe6f0")
        self.result_label.grid(row=10, column=0, columnspan=4, pady=5)

        root.bind("<Return>", lambda event: self.add_run())

        self.refresh_list()

    from datetime import datetime

    def add_run(self):
        """add new run or update existing one"""
        try:
            distance = float(self.distance_entry.get())
            minutes = float(self.minutes_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Distance and minutes must be numbers")
            return

        if distance <= 0 or minutes <= 0:
            messagebox.showerror("Error", "Distance and minutes must be positive")
            return

        date = self.date_entry.get()

        if not date:
            messagebox.showerror("Error", "Date cannot be empty")
            return

        try:
            datetime.strptime(date, "%d.%m.%Y")
        except ValueError:
            messagebox.showerror("Error", "Invalid date. Use format dd.mm.yyyy")
            return

        if self.editing_id:
            self.app.update_run(self.editing_id, distance, minutes, date)
            self.editing_id = None
            self.add_button.config(text="Add Run")
        else:
            self.app.add_run(distance, minutes, date)

        self.refresh_list()
        self.clear_fields()

    def delete_run(self):
        """delete selected run"""
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Select a run first")
            return

        index = selection[0]
        run_id = self.runs[index].id

        self.app.delete_run(run_id)
        self.refresh_list()

    def load_selected(self):
        """load selected run data into input fields for editing"""
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Select a run first")
            return

        index = selection[0]
        run = self.runs[index]

        self.editing_id = run.id

        self.distance_entry.delete(0, tk.END)
        self.distance_entry.insert(0, run.distance)

        self.minutes_entry.delete(0, tk.END)
        self.minutes_entry.insert(0, run.minutes)

        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, run.date)
        self.add_button.config(text="Update Run")

    def total_distance(self):
        """calculate total distance of all runs"""
        total = self.app.distance_total()
        self.result_label.config(text=f"Total distance: {total} km")

    def average_pace(self):
        """calculate average pace of all runs"""
        pace = self.app.average_pace()

        if pace is None:
            self.result_label.config(text="No runs available")
            return

        minutes = int(pace)
        seconds = int((pace - minutes) * 60)

        self.result_label.config(
            text=f"Average pace: {minutes}:{seconds:02d} min/km"
        )

    def longest_run(self):
        """find longest run and display it"""
        run = self.app.longest_run()
        if run:
            self.result_label.config(text=f"Longest run: {run.distance} km on {run.date}")
        else:
            self.result_label.config(text="No runs found")

  
    def average_distance(self):
        """find average distance of all runs and display it"""
        avg = self.app.average_distance()

        if avg == 0:
            self.result_label.config(text="No runs available")
            return

        self.result_label.config(text=f"Average distance: {round(avg, 2)} km")

        
    def search_by_date(self):
        """search runs by date and display them"""
        date = self.date_entry.get()
        runs = self.app.find_date(date)

        self.listbox.delete(0, tk.END)
        self.runs = runs

        if not runs:
            self.result_label.config(text="No runs found")
            return
        else:
            self.result_label.config(text="")

        for run in runs:
            text = f"{run.distance} km, {run.minutes} min, {run.date}"
            self.listbox.insert(tk.END, text)

    def refresh_list(self):
        """refresh the listbox with all runs"""
        self.listbox.delete(0, tk.END)

        self.runs = self.app.list_runs()

        for run in self.runs:
            text = f"{run.distance} km, {run.minutes} min, {run.date}"
            self.listbox.insert(tk.END, text)

    def fastest_run(self):
        """find fastest run and based on pace and display it"""
        run = self.app.fastest_run()
        if run:
            pace = run.pace()
            self.result_label.config(text=f"Fastest run: {run.distance} km on {run.date} with pace {run.pace_str()} min/km")
        else:
            self.result_label.config(text="No runs found")

    def clear_fields(self):
        """clear all input fields and reset editing state"""
        self.distance_entry.delete(0, tk.END)
        self.minutes_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.editing_id = None
        self.add_button.config(text="Add Run")

    def sort_by_distance(self):
        """sort runs by distance and display them"""
        runs = self.app.sort_by_distance()
        self.update_listbox(runs)

    def sort_by_date(self):
        """sort runs by date and display them"""
        runs = self.app.sort_by_date()
        self.update_listbox(runs)

    def update_listbox(self, runs):
        """helper method to update listbox with given runs"""
        self.listbox.delete(0, tk.END)
        self.runs = runs

        for run in runs:
            text = f"{run.distance} km, {run.minutes} min, {run.date}"
            self.listbox.insert(tk.END, text)

    def show_details(self, event):
        """open a new window showing details of the selected run"""
        selection = self.listbox.curselection()
        if not selection:
            return

        index = selection[0]
        run = self.runs[index]

        pace = run.pace()
        speed = run.speed()

        window = tk.Toplevel()
        window.title("Run details")

        tk.Label(window, text=f"Date: {run.date}").pack(pady=5)
        tk.Label(window, text=f"Distance: {run.distance} km").pack(pady=5)
        tk.Label(window, text=f"Time: {run.minutes} min").pack(pady=5)
        tk.Label(window, text=f"Pace: {run.pace_str()} min/km").pack(pady=5)
        tk.Label(window, text=f"Speed: {round(speed, 2)} km/h").pack(pady=5)

    def show_graph(self):
        """show a graph of all runs"""
        runs = self.app.list_runs()

        if not runs:
            messagebox.showinfo("Info", "No runs to display")
            return

        show_distance_graph(runs)


    def show_selected_pace(self):
        """show a graph of pace for the selected run"""
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Select a run first")
            return

        if not self.runs:
            messagebox.showinfo("Info", "No runs to display")
            return

        run = self.runs[selection[0]]
        show_selected_pace_graph(run)


    def show_graph_with_selected(self):
        """show a graph of all runs with the selected run highlighted"""
        runs = self.app.list_runs()

        if not runs:
            messagebox.showinfo("Info", "No runs to display")
            return

        selection = self.listbox.curselection()
        selected_id = None

        if selection:
            selected_id = self.runs[selection[0]].id

        show_graph_with_highlight(runs, selected_id)


def main():
    init_db()
    root = tk.Tk()
    RunGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()