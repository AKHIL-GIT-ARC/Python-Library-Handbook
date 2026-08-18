# CSV - Examples

import csv

# 1. Reading CSV with reader()
print("1. Reading CSV")
with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 2. Writing CSV with writer()
print("\n2. Writing CSV")
rows = [
    ["name", "age", "course"],
    ["Akhil", 20, "CSE"],
    ["Rahul", 21, "IT"]
]
with open("students_output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
print("CSV file created.")

# 3. Writing one row with writerow()
print("\n3. writerow()")
with open("student_single.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age"])
    writer.writerow(["Akhil", 20])
print("Rows written.")

# 4. Reading with DictReader
print("\n4. DictReader")
with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["course"])

# 5. Writing with DictWriter
print("\n5. DictWriter")
fields = ["name", "age", "course"]
with open("students_dict.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerow({
        "name": "Akhil",
        "age": 20,
        "course": "CSE"
    })
    writer.writerow({
        "name": "Rahul",
        "age": 21,
        "course": "IT"
    })
print("Dictionary CSV created.")