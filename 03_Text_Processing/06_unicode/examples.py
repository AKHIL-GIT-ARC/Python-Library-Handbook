# Unicode - Examples

# 1. Unicode Characters

text = "Hello 世界 ₹ 😀"
print(text)

# 2. ord()
print("\nord():")
print(ord("A"))
print(ord("₹"))
print(ord("😀"))

# 3. chr()
print("\nchr():")
print(chr(65))
print(chr(8377))
print(chr(128512))

# 4. Unicode Escape Sequences
print("\nUnicode Escape:")
print("\u0041")
print("\u20B9")
print("\U0001F600")

# 5. Character to Code Point
print("\nCharacter → Code Point:")
character = "A"
code = ord(character)
print("Character:", character)
print("Code Point:", code)

# 6. Code Point to Character
print("\nCode Point → Character:")
code = 8377
character = chr(code)
print("Code Point:", code)
print("Character:", character)

# 7. Multiple Characters
print("\nMultiple Characters:")
text = "Python ₹ © 😀"
for character in text:
    print(character, "→", ord(character))