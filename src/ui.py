from run import RunApp

app = RunApp()

while True:
    print()
    print("1 add run")
    print("2 list runs")
    print("3 delete run")
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
            print(i, run.distance, run.minutes, run.date, run.pace())

    elif command == "3":
        index = int(input("index: "))
        app.delete_run(index)

    elif command == "0":
        break