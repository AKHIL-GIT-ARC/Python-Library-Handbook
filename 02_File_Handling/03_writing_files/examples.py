# Writing Files - Examples

# 1. write() - Write text
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python")
print("Text written successfully.")

# 2. Write multiple lines
with open("languages.txt", "w", encoding="utf-8") as file:
    file.write("Python\n")
    file.write("Java\n")
    file.write("C++\n")
print("Multiple lines written.")

# 3. writelines() - Write a list of strings
languages = [
    "Python\n",
    "Java\n",
    "C++\n"
]
with open("languages.txt", "w", encoding="utf-8") as file:
    file.writelines(languages)
print("List written using writelines().")

# 4. Append data
with open("languages.txt", "a", encoding="utf-8") as file:
    file.write("JavaScript\n")
print("New data appended.")

# 5. Write variables
name = "Akhil"
marks = 90
with open("student.txt", "w", encoding="utf-8") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Marks: {marks}\n")
print("Student data written.")

# 6. write() return value
with open("message.txt", "w", encoding="utf-8") as file:
    characters_written = file.write("Hello Python")
print("Characters written:", characters_written)