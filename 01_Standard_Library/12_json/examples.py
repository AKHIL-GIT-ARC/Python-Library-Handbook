import json
from pathlib import Path
print("===== JSON Module Examples =====")
json_file = Path("data/students.json")
students = [
    {
        "name": "Akhil",
        "age": 19,
        "course": "CSE"
    },
    {
        "name": "Charan",
        "age": 19,
        "course": "AIML"
    }
]

# ---------------------------------------
# 1. dump()
# ---------------------------------------

print("\n1. dump()")
with open(json_file, "w") as file:
    json.dump(students, file, indent=4)
print("Data Written Successfully")

# ---------------------------------------
# 2. load()
# ---------------------------------------

print("\n2. load()")
with open(json_file, "r") as file:
    data = json.load(file)
print(data)

# ---------------------------------------
# 3. dumps()
# ---------------------------------------

print("\n3. dumps()")
json_string = json.dumps(students, indent=4)
print(json_string)

# ---------------------------------------
# 4. loads()
# ---------------------------------------

print("\n4. loads()")
python_data = json.loads(json_string)
print(python_data)

# ---------------------------------------
# 5. Pretty Printing
# ---------------------------------------

print("\n5. Pretty Printing")
print(json.dumps(students, indent=4))