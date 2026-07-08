import calendar

while True:
    print("\n" + "=" * 30)
    print("      CALENDAR UTILITY PRO")
    print("=" * 30)
    print("1. View Monthly Calendar")
    print("2. View Year Calendar")
    print("3. Check Leap Year")
    print("4. Find Weekday")
    print("5. Days in a Month")
    print("6. Display Month Names")
    print("7. Display Weekday Names")
    print("8. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        year = int(input("Enter Year: "))
        month = int(input("Enter Month (1-12): "))
        print("\n")
        print(calendar.month(year, month))

    elif choice == "2":
        year = int(input("Enter Year: "))
        print("\n")
        print(calendar.calendar(year))

    elif choice == "3":
        year = int(input("Enter Year: "))
        if calendar.isleap(year):
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is NOT a Leap Year.")

    elif choice == "4":
        year = int(input("Enter Year: "))
        month = int(input("Enter Month: "))
        day = int(input("Enter Day: "))
        weekday = calendar.weekday(year, month, day)
        print("Weekday:", calendar.day_name[weekday])

    elif choice == "5":
        year = int(input("Enter Year: "))
        month = int(input("Enter Month: "))
        first_day, total_days = calendar.monthrange(year, month)
        print("First Day :", calendar.day_name[first_day])
        print("Total Days:", total_days)

    elif choice == "6":
        print("\nMonth Names")
        for month in calendar.month_name[1:]:
            print(month)

    elif choice == "7":
        print("\nWeekday Names")
        for day in calendar.day_name:
            print(day)

    elif choice == "8":
        print("\nThank you for using Calendar Utility Pro!")
        break
    else:
        print("Invalid Choice! Please try again.")