import glob

print("===== Glob Module Examples =====")

# ---------------------------------------
# 1. Find Python Files
# ---------------------------------------

print("\n1. Python Files")
python_files = glob.glob("practice_files/python/*.py")
for file in python_files:
    print(file)

# ---------------------------------------
# 2. Find Text Files
# ---------------------------------------

print("\n2. Text Files")
text_files = glob.glob("practice_files/text/*.txt")
for file in text_files:
    print(file)

# ---------------------------------------
# 3. Find Image Files
# ---------------------------------------

print("\n3. Image Files")
image_files = glob.glob("practice_files/images/*")
for file in image_files:
    print(file)

# ---------------------------------------
# 4. Wildcard (*)
# ---------------------------------------

print("\n4. Wildcard (*)")
all_files = glob.glob("practice_files/*")
for file in all_files:
    print(file)

# ---------------------------------------
# 5. Single Character (?)
# ---------------------------------------

print("\n5. Single Character (?)")
files = glob.glob("practice_files/python/????.py")
for file in files:
    print(file)

# ---------------------------------------
# 6. Character Range []
# ---------------------------------------

print("\n6. Character Range []")

files = glob.glob("practice_files/text/[nr]*.txt")
for file in files:
    print(file)

# ---------------------------------------
# 7. Recursive Search
# ---------------------------------------

print("\n7. Recursive Search")
files = glob.glob("practice_files/**/*.py", recursive=True)
for file in files:
    print(file)

# ---------------------------------------
# 8. Iterator Search
# ---------------------------------------

print("\n8. Iterator Search")
for file in glob.iglob("practice_files/**/*.py", recursive=True):
    print(file)