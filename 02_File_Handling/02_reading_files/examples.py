# Reading Files - Examples

FILE_NAME = "sample.txt"

# 1. read() - Read entire file
with open(FILE_NAME, "r", encoding="utf-8") as file:
    content = file.read()
print("Entire File:")
print(content)


# 2. read(n) - Read limited characters
with open(FILE_NAME, "r", encoding="utf-8") as file:
    content = file.read(6)
print("\nFirst 6 characters:")
print(content)


# 3. readline() - Read one line
with open(FILE_NAME, "r", encoding="utf-8") as file:
    first = file.readline().strip()
    second = file.readline().strip()
print("\nFirst line:", first)
print("Second line:", second)


# 4. readlines() - Read lines into a list
with open(FILE_NAME, "r", encoding="utf-8") as file:
    lines = file.readlines()
print("\nList of lines:")
print(lines)


# 5. Read line by line
print("\nLine by line:")
with open(FILE_NAME, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


# 6. tell() - Check current position
with open(FILE_NAME, "r", encoding="utf-8") as file:
    print("\nStart position:", file.tell())
    file.read(6)
    print("Position after read:", file.tell())


# 7. seek() - Return to beginning
with open(FILE_NAME, "r", encoding="utf-8") as file:
    print("\nFirst read:", file.read(6))
    file.seek(0)
    print("After seek:", file.read(6))


# 8. Add line numbers
print("\nLines with numbers:")
with open(FILE_NAME, "r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number}. {line.strip()}")