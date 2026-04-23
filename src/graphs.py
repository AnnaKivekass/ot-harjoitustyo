import matplotlib.pyplot as plt

def show_distance_graph(runs):
    """show a graph of all run distances"""
    distances = [run.distance for run in runs]

    plt.figure()
    dates = [run.date for run in runs]
    plt.plot(distances)
    plt.xticks(range(len(dates)), dates, rotation=45)
    plt.title("Run distances")
    plt.xlabel("Run")
    plt.ylabel("Distance (km)")
    plt.show()


def show_selected_pace_graph(run):
    """show a graph of the selected run's pace"""
    pace = run.pace()

    plt.figure()
    plt.bar(["Selected Run"], [pace])
    plt.ylabel("Pace (min/km)")
    plt.title("Pace of selected run")
    plt.show()


def show_graph_with_highlight(runs, selected_id=None):
    """show a graph of all run distances, highlighting the selected run"""
    distances = [run.distance for run in runs]

    plt.figure()
    plt.plot(distances)

    if selected_id:
        for i, run in enumerate(runs):
            if run.id == selected_id:
                plt.scatter(i, distances[i], s=100, color="red")
                break

    plt.title("Run distances (selected run highlighted)")
    plt.show()