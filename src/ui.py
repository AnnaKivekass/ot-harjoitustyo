from run import RunApp

app = RunApp()

while True:
    print()
    print("1 add run")
    print("2 list runs")
    print("3 delete run")
    print("4 total distance")
    print("5 average pace")
    print("6 longest run")
    print("7 search by date")
    print("8 average distance")
    print("0 exit")

    command = input("choose: ")

    if command == "1":
        distance = float(input("distance (in km): "))
        minutes = float(input("duration (in minutes): "))
        date = input("date: ")
        app.add_run(distance, minutes, date)

    elif command == "2":
        runs = app.list_runs()
        for i, run in enumerate(runs):
            print(f"{i}: {run.distance} km, {run.minutes} min, {run.date}, pace {round(run.pace(),2)} min/km, speed {round(run.speed(),2)} km/h")

    elif command == "3":
        index = int(input("index: "))
        app.delete_run(index)
    

    elif command == "4":
        print(f"total distance: {app.distance_total()} km")

    elif command == "5":
        print(f"average pace: {round(app.average_pace(),2)} min/km")

    elif command == "6":
        run = app.longest_run()
        if run:
            print(f"longest run: {run.distance} km on {run.date}")

    elif command == "7":
        date = input("date: ")
        runs = app.find_date(date)

        for run in runs:
            print(f"{run.distance} km, {run.minutes} min, pace {round(run.pace(),2)}")

    elif command == "8":
        print(f"average distance: {round(app.average_distance(),2)} km")

    elif command == "0":
        break