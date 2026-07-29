"""
examples.py
Module: File Basics

"""
# -----------------------------------------
# 1. Creating and Writing to a File
# -----------------------------------------
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Hello, Python!")
print("File created and data written.")

# -----------------------------------------
# 2. Reading a File
# -----------------------------------------
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("\nFile Content:")
print(content)

# -----------------------------------------
# 3. Appending to a File
# -----------------------------------------
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("\nLearning File Handling.")
print("\nNew data appended.")

# -----------------------------------------
# 4. Reading After Appending
# -----------------------------------------
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("\nUpdated File Content:")
print(content)

# -----------------------------------------
# 5. Using open() and close()
# -----------------------------------------
file = open("notes.txt", "r", encoding="utf-8")
content = file.read()
print("\nUsing open() manually:")
print(content)
file.close()

# -----------------------------------------
# 6. Checking Whether File is Closed
# -----------------------------------------
file = open("notes.txt", "r", encoding="utf-8")
print("\nBefore close():", file.closed)
file.close()
print("After close():", file.closed)

# -----------------------------------------
# 7. File Object Properties
# -----------------------------------------
with open("notes.txt", "r", encoding="utf-8") as file:
    print("\nFile Properties:")
    print("Name:", file.name)
    print("Mode:", file.mode)
    print("Closed:", file.closed)
print("Closed after with block:", file.closed)

# -----------------------------------------
# 8. Write Multiple Lines
# -----------------------------------------
with open("languages.txt", "w", encoding="utf-8") as file:
    file.write("Python\n")
    file.write("Java\n")
    file.write("C++\n")
print("\nMultiple lines written.")

# -----------------------------------------
# 9. Read Multiple Lines
# -----------------------------------------
with open("languages.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("\nLanguages:")
print(content)

# -----------------------------------------
# 10. Create Mode
# -----------------------------------------
try:
    with open(
        "new_file.txt",
        "x",
        encoding="utf-8"
    ) as file:
        file.write("This file was created using x mode.")
    print("new_file.txt created.")
except FileExistsError:
    print(
        "\nnew_file.txt already exists."
    )

# -----------------------------------------
# 11. FileNotFoundError
# -----------------------------------------
try:
    with open(
        "missing_file.txt",
        "r",
        encoding="utf-8"
    ) as file:
        print(file.read())
except FileNotFoundError:
    print(
        "\nmissing_file.txt was not found."
    )

# -----------------------------------------
# 12. Simple Student Record
# -----------------------------------------
name = "Akhil"
marks = 90
with open(
    "student.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(f"Name: {name}\n")
    file.write(f"Marks: {marks}")
with open(
    "student.txt",
    "r",
    encoding="utf-8"
) as file:
    print("\nStudent Record:")
    print(file.read())
