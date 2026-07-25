"""
mini_project.py
Module: argparse

Student CLI Manager
"""

import argparse
# -----------------------------------------
# Create Parser
# -----------------------------------------
parser = argparse.ArgumentParser(
    description="Student CLI Manager"
)

# -----------------------------------------
# Action Argument
# -----------------------------------------
parser.add_argument(
    "action",
    choices=["add", "list", "search", "delete"],
    help="Action to perform"
)

# -----------------------------------------
# Student Name
# -----------------------------------------
parser.add_argument(
    "name",
    nargs="?",
    help="Student name"
)

# -----------------------------------------
# Optional Department
# -----------------------------------------
parser.add_argument(
    "--department",
    choices=["CSE", "ECE", "ME", "CE"],
    help="Student department"
)

# -----------------------------------------
# Verbose Flag
# -----------------------------------------
parser.add_argument(
    "--verbose",
    action="store_true",
    help="Show additional details"
)

# -----------------------------------------
# Parse Arguments
# -----------------------------------------
args = parser.parse_args()

# -----------------------------------------
# Student Data
# -----------------------------------------
students = [
    {"name": "Charan", "department": "CSE"},
    {"name": "Kiran", "department": "ECE"}
]

# -----------------------------------------
# Add Student
# -----------------------------------------
def add_student():
    if not args.name:
        print("Please provide a student name.")
        return
    student = {
        "name": args.name,
        "department": args.department
    }
    students.append(student)
    print(f"Student '{args.name}' added successfully.")
    if args.verbose:
        print("Student Details:", student)

# -----------------------------------------
# List Students
# -----------------------------------------
def list_students():
    print("\nStudent List")
    for student in students:
        print(
            student["name"],
            "-",
            student["department"]
        )

# -----------------------------------------
# Search Student
# -----------------------------------------
def search_student():
    if not args.name:
        print("Please provide a student name.")
        return
    for student in students:
        if student["name"].lower() == args.name.lower():
            print("Student Found!")
            print("Name       :", student["name"])
            print("Department :", student["department"])
            return
    print("Student not found.")

# -----------------------------------------
# Delete Student
# -----------------------------------------
def delete_student():
    if not args.name:
        print("Please provide a student name.")
        return
    for student in students:
        if student["name"].lower() == args.name.lower():
            students.remove(student)
            print(f"Student '{student['name']}' deleted.")
            return
    print("Student not found.")

# -----------------------------------------
# Perform Selected Action
# -----------------------------------------
if args.action == "add":
    add_student()
elif args.action == "list":
    list_students()
elif args.action == "search":
    search_student()
elif args.action == "delete":
    delete_student()