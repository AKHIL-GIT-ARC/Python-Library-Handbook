import time


def stopwatch():
    print("\n===== Stopwatch =====")
    input("Press ENTER to start...")
    start = time.perf_counter()
    input("Press ENTER to stop...")
    end = time.perf_counter()
    print(f"\nElapsed Time: {end - start:.2f} seconds")


def countdown():
    print("\n===== Countdown Timer =====")
    seconds = int(input("Enter countdown time (seconds): "))
    while seconds > 0:
        print(f"Time Left: {seconds} sec")
        time.sleep(1)
        seconds -= 1
    print("Time's Up!")


def pomodoro():
    print("\n===== Pomodoro Timer =====")
    minutes = int(input("Enter session time (minutes): "))
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins = total_seconds // 60
        secs = total_seconds % 60

        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("\nSession Complete!")


def execution_timer():
    print("\n===== Execution Timer =====")
    start = time.perf_counter()
    total = 0
    for i in range(1000000):
        total += i
    end = time.perf_counter()
    print(f"Execution Time: {end - start:.6f} seconds")


def current_time():
    print("\n===== Current Time =====")
    print("Local Time :", time.ctime())
    print("Formatted :", time.strftime("%d-%m-%Y %I:%M:%S %p"))


while True:
    print("\n" + "=" * 30)
    print("      PRODUCTIVITY TIMER")
    print("=" * 30)

    print("1. Stopwatch")
    print("2. Countdown Timer")
    print("3. Pomodoro Timer")
    print("4. Measure Code Execution Time")
    print("5. Current Local Time")
    print("6. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        stopwatch()
    elif choice == "2":
        countdown()
    elif choice == "3":
        pomodoro()
    elif choice == "4":
        execution_timer()
    elif choice == "5":
        current_time()
    elif choice == "6":
        print("\nThank you for using Productivity Timer!")
        break
    else:
        print("\nInvalid Choice!")