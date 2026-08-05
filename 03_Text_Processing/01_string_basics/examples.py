# String Basics - Examples

text = "Python Programming"
# -------------------------------
# 1. Creating Strings
# -------------------------------
print("1. Creating Strings")
single = 'Python'
double = "Programming"
multi = """Welcome
to
Python"""
print(single)
print(double)
print(multi)

# -------------------------------
# 2. Indexing
# -------------------------------
print("\n2. Indexing")
print("First Character :", text[0])
print("Fourth Character:", text[3])

# -------------------------------
# 3. Negative Indexing
# -------------------------------
print("\n3. Negative Indexing")
print("Last Character :", text[-1])
print("Second Last    :", text[-2])

# -------------------------------
# 4. Slicing
# -------------------------------
print("\n4. Slicing")
print(text[0:6])
print(text[7:])
print(text[:6])
print(text[-11:])

# -------------------------------
# 5. String Length
# -------------------------------
print("\n5. Length")
print(len(text))

# -------------------------------
# 6. Concatenation
# -------------------------------
print("\n6. Concatenation")
first = "Hello"
second = "World"
print(first + " " + second)

# -------------------------------
# 7. Repetition
# -------------------------------
print("\n7. Repetition")
print("Python " * 3)

# -------------------------------
# 8. Membership
# -------------------------------
print("\n8. Membership")
print("Python" in text)
print("Java" in text)
print("Java" not in text)

# -------------------------------
# 9. Immutability
# -------------------------------
print("\n9. Immutability")
word = "Python"
new_word = "J" + word[1:]
print("Original :", word)
print("Modified :", new_word)