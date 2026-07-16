import csv
from pathlib import Path
CSV_FILE = Path("data/employees.csv")
FIELDNAMES = ["ID", "Name", "Age", "Department"]

def initialize_file():
    if not CSV_FILE.exists() or CSV_FILE.stat().st_size == 0:
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

def load_employees():
    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_employees(employees):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(employees)

def add_employee():
    employees = load_employees()
    employee = {
        "ID": input("Enter ID: "),
        "Name": input("Enter Name: "),
        "Age": input("Enter Age: "),
        "Department": input("Enter Department: ")
    }
    employees.append(employee)
    save_employees(employees)
    print("Employee Added Successfully.")

def view_employees():
    employees = load_employees()
    if not employees:
        print("No Employee Records Found.")
        return
    print("\nEmployee Records")
    for employee in employees:
        print(employee)

def search_employee():
    employees = load_employees()
    name = input("Enter Employee Name: ")
    for employee in employees:
        if employee["Name"].lower() == name.lower():
            print(employee)
            return
    print("Employee Not Found.")


def update_employee():
    employees = load_employees()
    emp_id = input("Enter Employee ID: ")
    for employee in employees:
        if employee["ID"] == emp_id:
            employee["Name"] = input("Enter New Name: ")
            employee["Age"] = input("Enter New Age: ")
            employee["Department"] = input("Enter New Department: ")
            save_employees(employees)
            print("Employee Updated Successfully.")
            return
    print("Employee Not Found.")


def delete_employee():
    employees = load_employees()
    emp_id = input("Enter Employee ID: ")
    for employee in employees:
        if employee["ID"] == emp_id:
            employees.remove(employee)
            save_employees(employees)
            print("Employee Deleted Successfully.")
            return
    print("Employee Not Found.")

initialize_file()
while True:

    print("\n" + "=" * 40)
    print("      EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("\nEnter Choice: ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("\nThank you for using Employee Management System!")
        break
    else:
        print("Invalid Choice! Please try again.")