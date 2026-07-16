import csv
from pathlib import Path

print("===== CSV Module Examples =====")

csv_file = Path("data/employees.csv")
employees = [
    [101, "Akhil", 20, "CSE"],
    [102, "Chakri", 21, "AIML"],
    [103, "OM", 19, "CSE"]
]

# ---------------------------------------
# 1. csv.writer()
# ---------------------------------------

print("\n1. csv.writer()")
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(employees)
print("Employee Records Added")

# ---------------------------------------
# 2. csv.reader()
# ---------------------------------------

print("\n2. csv.reader()")
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# ---------------------------------------
# 3. csv.DictReader()
# ---------------------------------------

print("\n3. csv.DictReader()")
with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# ---------------------------------------
# 4. csv.DictWriter()
# ---------------------------------------

print("\n4. csv.DictWriter()")
csv_file2 = Path("data/employees_dict.csv")
employees_dict = [
    {
        "ID": 201,
        "Name": "BOB",
        "Age": 50,
        "Department": "HR"
    },
    {
        "ID": 202,
        "Name": "Ali",
        "Age": 20,
        "Department": "Finance"
    }
]
with open(csv_file2, "w", newline="") as file:
    fieldnames = ["ID", "Name", "Age", "Department"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employees_dict)
print("Dictionary Data Written")
