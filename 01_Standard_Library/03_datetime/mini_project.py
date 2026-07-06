from datetime import datetime, timedelta


def current_datetime():
    now = datetime.now()
    print("\nCurrent Date :", now.strftime("%d-%m-%Y"))
    print("Current Time :", now.strftime("%I:%M:%S %p"))


def calculate_age():
    dob = input("\nEnter DOB (DD-MM-YYYY): ")
    birth = datetime.strptime(dob, "%d-%m-%Y")
    today = datetime.today()
    age = today.year - birth.year
    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1
    print(f"Your Age : {age} years")


def date_difference():
    first = input("\nEnter First Date (DD-MM-YYYY): ")
    second = input("Enter Second Date (DD-MM-YYYY): ")
    d1 = datetime.strptime(first, "%d-%m-%Y")
    d2 = datetime.strptime(second, "%d-%m-%Y")
    print("Difference :", abs((d2 - d1).days), "days")


def weekday():
    user_date = input("\nEnter Date (DD-MM-YYYY): ")
    date = datetime.strptime(user_date, "%d-%m-%Y")
    print("Day :", date.strftime("%A"))


def add_days():
    user_date = input("\nEnter Date (DD-MM-YYYY): ")
    days = int(input("Enter Number of Days: "))
    date = datetime.strptime(user_date, "%d-%m-%Y")
    new_date = date + timedelta(days=days)
    print("New Date :", new_date.strftime("%d-%m-%Y"))


while True:
    print("\n" + "=" * 40)
    print("     DATE & AGE UTILITY TOOLKIT")
    print("=" * 40)
    print("1. Current Date & Time")
    print("2. Calculate Age")
    print("3. Days Between Two Dates")
    print("4. Find Day of the Week")
    print("5. Add Days to a Date")
    print("6. Exit")
    choice = input("\nEnter Choice: ")
    if choice == "1":
        current_datetime()
    elif choice == "2":
        calculate_age()
    elif choice == "3":
        date_difference()
    elif choice == "4":
        weekday()
    elif choice == "5":
       add_days()
    elif choice == "6":
        print("\nThank you!")
        break
    else:
        print("\nInvalid Choice!")