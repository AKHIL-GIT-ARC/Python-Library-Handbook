# File Modes - Examples

# -------------------------------
# 1. Read Mode (r)
# -------------------------------
print("1. Read Mode (r)")
with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())

# -------------------------------
# 2. Write Mode (w)
# -------------------------------
print("\n2. Write Mode (w)")
with open("write_demo.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python")
print("Data written successfully.")

# -------------------------------
# 3. Append Mode (a)
# -------------------------------
print("\n3. Append Mode (a)")
with open("write_demo.txt", "a", encoding="utf-8") as file:
    file.write("\nFile Handling")
print("Data appended successfully.")

# -------------------------------
# 4. Create Mode (x)
# -------------------------------
print("\n4. Create Mode (x)")
try:
    with open("new_file.txt", "x", encoding="utf-8") as file:
        file.write("New File Created")
    print("File created successfully.")
except FileExistsError:
    print("File already exists.")

# -------------------------------
# 5. Read & Write (r+)
# -------------------------------
print("\n5. Read & Write (r+)")
with open("notes.txt", "r+", encoding="utf-8") as file:
    print(file.read())
    file.write("\nPython")

# -------------------------------
# 6. Write & Read (w+)
# -------------------------------
print("\n6. Write & Read (w+)")
with open("demo.txt", "w+", encoding="utf-8") as file:
    file.write("Python")
    file.seek(0)
    print(file.read())

# -------------------------------
# 7. Append & Read (a+)
# -------------------------------
print("\n7. Append & Read (a+)")
with open("demo.txt", "a+", encoding="utf-8") as file:
    file.write("\nJava")
    file.seek(0)
    print(file.read())

# -------------------------------
# 8. Binary Mode (rb)
# -------------------------------
print("\n8. Binary Mode (rb)")
try:
    with open("image.jpg", "rb") as file:
        data = file.read(10)
    print(data)
except FileNotFoundError:
    print("image.jpg not found.")