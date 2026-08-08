# Regular Expressions - Examples

import re

# 1. re.search()
text = "My age is 20"
result = re.search(r"\d+", text)
if result:
    print("Search:", result.group())


# 2. re.match()
result = re.match(r"Hello", "Hello Python")
if result:
    print("Match:", result.group())


# 3. re.findall()
text = "A12 B34 C56"
numbers = re.findall(r"\d+", text)
print("Numbers:", numbers)


# 4. re.sub()
text = "Python is difficult"
result = re.sub(r"difficult", "easy", text)
print("Replace:", result)


# 5. re.split()
text = "Python,Java;C++"
languages = re.split(r"[,;]", text)
print("Split:", languages)


# 6. Character Classes
text = "Python ABC 123"
print("Uppercase:", re.findall(r"[A-Z]", text))
print("Digits:", re.findall(r"[0-9]", text))
print("Lowercase:", re.findall(r"[a-z]", text))


# 7. Quantifiers
text = "A1 B22 C333"
print("1+ digits:", re.findall(r"\d+", text))
print("Exactly 2 digits:", re.findall(r"\d{2}", text))


# 8. Groups
text = "Name: Akhil"
result = re.search(r"Name: (\w+)", text)
if result:
    print("Name:", result.group(1))


# 9. Email Validation
email = "student@example.com"
pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
print("Valid email:", bool(re.match(pattern, email)))


# 10. Phone Number Extraction
text = "Contact: 9876543210"
phone = re.findall(r"\d{10}", text)
print("Phone:", phone)