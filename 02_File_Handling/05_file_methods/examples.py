# File Methods - Examples

# -------------------------------
# 1. close()
# -------------------------------
print("1. close()")
file = open("notes.txt", "r", encoding="utf-8")
print("Before closing:", file.closed)
file.close()
print("After closing:", file.closed)

# -------------------------------
# 2. flush()
# -------------------------------
print("\n2. flush()")
with open("flush_demo.txt", "w", encoding="utf-8") as file:
    file.write("Python")
    file.flush()
print("Data flushed successfully.")

# -------------------------------
# 3. truncate()
# -------------------------------
print("\n3. truncate()")
with open("truncate_demo.txt", "w+", encoding="utf-8") as file:
    file.write("Python Programming")
    file.truncate(6)
with open("truncate_demo.txt", "r", encoding="utf-8") as file:
    print(file.read())

# -------------------------------
# 4. readable()
# -------------------------------
print("\n4. readable()")
with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.readable())

# -------------------------------
# 5. writable()
# -------------------------------
print("\n5. writable()")
with open("write_demo.txt", "w", encoding="utf-8") as file:
    print(file.writable())

# -------------------------------
# 6. seekable()
# -------------------------------
print("\n6. seekable()")
with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.seekable())

# -------------------------------
# 7. fileno()
# -------------------------------
print("\n7. fileno()")
with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.fileno())

# -------------------------------
# 8. isatty()
# -------------------------------
print("\n8. isatty()")
with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.isatty())