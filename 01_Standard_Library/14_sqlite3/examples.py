import sqlite3
from pathlib import Path

print("===== SQLite3 Module Examples =====")
db_file = Path("database/students.db")

# ---------------------------------------
# 1. Connect to Database
# ---------------------------------------

print("\n1. Connect to Database")
connection = sqlite3.connect(db_file)
cursor = connection.cursor()
print("Database Connected")

# ---------------------------------------
# 2. Create Table
# ---------------------------------------

print("\n2. Create Table")
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")
connection.commit()
print("Table Created")

# ---------------------------------------
# 3. Insert One Record
# ---------------------------------------

print("\n3. Insert One Record")
cursor.execute("""
INSERT INTO students(name, age, course)
VALUES (?, ?, ?)
""", ("Akhil", "19", "AIML"))
connection.commit()
print("Record Inserted")

# ---------------------------------------
# 4. Insert Multiple Records
# ---------------------------------------

print("\n4. Insert Multiple Records")
students = [
    ("Charan", 20, "AIML"),
    ("Om", 19, "CSE")
]
cursor.executemany("""
INSERT INTO students(name, age, course)
VALUES (?, ?, ?)
""", students)
connection.commit()
print("Multiple Records Inserted")

# ---------------------------------------
# 5. View All Records
# ---------------------------------------

print("\n5. View All Records")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# ---------------------------------------
# 6. View One Record
# ---------------------------------------

print("\n6. View One Record")
cursor.execute("SELECT * FROM students WHERE id = 1")
row = cursor.fetchone()
print(row)

# ---------------------------------------
# 7. Update Record
# ---------------------------------------

print("\n7. Update Record")
cursor.execute("""
UPDATE students
SET course = ?
WHERE name = ?
""", ("AI & ML", "Rahul"))
connection.commit()
print("Record Updated")

# ---------------------------------------
# 8. Delete Record
# ---------------------------------------

print("\n8. Delete Record")
cursor.execute("""
DELETE FROM students
WHERE name = ?
""", ("Om",))
connection.commit()
print("Record Deleted")

# ---------------------------------------
# 9. Close Database
# ---------------------------------------

print("\n9. Close Database")
connection.close()
print("Database Closed")