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

    elif command == "4":
        print("total distance: ", app.distance_total())

    elif command == "5":
        print("average pace:", round(app.average_pace(),2 ))

    elif command == "6":
        run = app.longest_run()
        if run:
            print("longest:", run.distance, run.date)

    elif command == "0":
        break