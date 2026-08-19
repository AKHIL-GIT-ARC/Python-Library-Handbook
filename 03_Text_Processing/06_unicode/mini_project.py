# Mini Project - Unicode Character Inspector

text = input("Enter text: ")
print("\n--- Unicode Inspector ---")
print("Text:", text)
print("Characters:", len(text))
print("\nCharacter Details:")
for character in text:
    print(f"{character} → U+{ord(character):04X}")
print("\nReconstructed Text:")
for character in text:
    print(chr(ord(character)), end="")
print()