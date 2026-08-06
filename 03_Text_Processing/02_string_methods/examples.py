# String Methods - Examples

text = "  python programming  "

# -------------------------------
# 1. upper()
# -------------------------------
print("1. upper()")
print(text.upper())

# -------------------------------
# 2. lower()
# -------------------------------
print("\n2. lower()")
print("PYTHON".lower())

# -------------------------------
# 3. title()
# -------------------------------
print("\n3. title()")
print(text.title())

# -------------------------------
# 4. capitalize()
# -------------------------------
print("\n4. capitalize()")
print(text.capitalize())

# -------------------------------
# 5. swapcase()
# -------------------------------
print("\n5. swapcase()")
print("Python".swapcase())

# -------------------------------
# 6. strip(), lstrip(), rstrip()
# -------------------------------
print("\n6. strip()")
print(text.strip())
print("\nlstrip()")
print(text.lstrip())
print("\nrstrip()")
print(text.rstrip())

# -------------------------------
# 7. replace()
# -------------------------------
print("\n7. replace()")
sentence = "I like Java"
print(sentence.replace("Java", "Python"))

# -------------------------------
# 8. find()
# -------------------------------
print("\n8. find()")
print(sentence.find("Java"))
print(sentence.find("C++"))

# -------------------------------
# 9. count()
# -------------------------------
print("\n9. count()")
language = "Python Python Java Python"
print(language.count("Python"))

# -------------------------------
# 10. startswith()
# -------------------------------
print("\n10. startswith()")
print(language.startswith("Python"))

# -------------------------------
# 11. endswith()
# -------------------------------
print("\n11. endswith()")
print(language.endswith("Python"))

# -------------------------------
# 12. split()
# -------------------------------
print("\n12. split()")
languages = "Python,Java,C++"
print(languages.split(","))

# -------------------------------
# 13. join()
# -------------------------------
print("\n13. join()")
items = ["Python", "Java", "C++"]
print(" | ".join(items))

# -------------------------------
# 14. Validation Methods
# -------------------------------
print("\n14. Validation Methods")
print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("python".islower())
print("PYTHON".isupper())
print("   ".isspace())