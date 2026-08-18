# Mini Project - Student CSV Manager

import csv

filename = "students.csv"
students = [
    {"name": "Akhil", "age": 20, "course": "CSE"},
    {"name": "Rahul", "age": 21, "course": "IT"},
    {"name": "Priya", "age": 20, "course": "CSE"}
]

# Write student data
with open(filename, "w", newline="") as file:
    fields = ["name", "age", "course"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)

# Read student data
print("----- Student Records -----")
with open(filename, "r", newline="") as file:
    reader = csv.DictReader(file)
    for student in reader:
        print(
            f"Name: {student['name']}, "
            f"Age: {student['age']}, "
            f"Course: {student['course']}"
        )