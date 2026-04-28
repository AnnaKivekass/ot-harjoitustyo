import matplotlib.pyplot as plt


def show_distance_graph(runs):
    """Show a graph of all run distances"""
    if not runs:
        return

    distances = [run.distance for run in runs]
    dates = [run.date for run in runs]

    plt.figure()
    plt.plot(distances, marker="o")
    plt.xticks(range(len(dates)), dates, rotation=45)
    plt.title("Run distances")
    plt.xlabel("Run")
    plt.ylabel("Distance (km)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def show_selected_pace_graph(run):
    """Show a graph of the selected run's pace"""
    if not run:
        return

    pace = run.pace()

    plt.figure()
    plt.bar(["Selected run"], [pace])
    plt.ylabel("Pace (min/km)")
    plt.title("Pace of selected run")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()


def show_graph_with_highlight(runs, selected_id=None):
    """Show a graph of all run distances, highlighting the selected run"""
    if not runs:
        return

    distances = [run.distance for run in runs]
    dates = [run.date for run in runs]

    plt.figure()
    plt.plot(distances, marker="o")

    if selected_id is not None:
        for i, run in enumerate(runs):
            if run.id == selected_id:
                plt.scatter(
                    i,
                    distances[i],
                    s=100,
                    color="red",
                    label="Selected run"
                )
                plt.legend()
                break

    plt.xticks(range(len(dates)), dates, rotation=45)
    plt.title("Run distances (selected run highlighted)")
    plt.xlabel("Run")
    plt.ylabel("Distance (km)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()