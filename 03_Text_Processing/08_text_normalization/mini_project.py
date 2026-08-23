# Mini Project - Text Normalizer

import unicodedata

text = input("Enter text: ")

# Normalize text
normalized = unicodedata.normalize("NFD", text)

# Remove combining marks
cleaned = "".join(
    char for char in normalized
    if not unicodedata.combining(char)
)

print("\n--- Text Normalizer ---")
print("Original  :", text)
print("Normalized:", normalized)
print("Cleaned   :", cleaned)

# Compare normalized text
nfc_text = unicodedata.normalize("NFC", text)

print("NFC Form  :", nfc_text)