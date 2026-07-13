import tempfile

print("===== Tempfile Module Examples =====")

# ---------------------------------------
# 1. System Temporary Directory
# ---------------------------------------

print("\n1. System Temporary Directory")
print(tempfile.gettempdir())

# ---------------------------------------
# 2. Temporary File
# ---------------------------------------

print("\n2. Temporary File")
with tempfile.TemporaryFile(mode="w+t") as file:
    file.write("Hello from Temporary File!")
    file.seek(0)
    print(file.read())
print("Temporary File Closed")

# ---------------------------------------
# 3. Named Temporary File
# ---------------------------------------

print("\n3. Named Temporary File")
with tempfile.NamedTemporaryFile(mode="w+t") as file:
    print("File Name:", file.name)
    file.write("Named Temporary File")
    file.seek(0)
    print(file.read())
print("Named Temporary File Closed")

# ---------------------------------------
# 4. Temporary Directory
# ---------------------------------------

print("\n4. Temporary Directory")
with tempfile.TemporaryDirectory() as folder:
    print(folder)
print("Temporary Directory Removed")

# ---------------------------------------
# 5. Spooled Temporary File
# ---------------------------------------

print("\n5. Spooled Temporary File")
with tempfile.SpooledTemporaryFile(mode="w+t") as file:
    file.write("Stored in Memory")
    file.seek(0)
    print(file.read())
print("Spooled Temporary File Closed")

# ---------------------------------------
# 6. Create Temporary File
# ---------------------------------------

print("\n6. mkstemp()")
fd, path = tempfile.mkstemp()
print("File Descriptor:", fd)
print("Path:", path)

# ---------------------------------------
# 7. Create Temporary Directory
# ---------------------------------------

print("\n7. mkdtemp()")
folder = tempfile.mkdtemp()
print(folder)