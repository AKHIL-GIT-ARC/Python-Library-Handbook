# Text Normalization - Examples

import unicodedata

# 1. NFC
text = "café"
nfc = unicodedata.normalize("NFC", text)
print("NFC:", nfc)

# 2. NFD
nfd = unicodedata.normalize("NFD", text)
print("NFD:", nfd)

# 3. NFKC
text = "①"
nfkc = unicodedata.normalize("NFKC", text)
print("NFKC:", nfkc)

# 4. NFKD
nfkd = unicodedata.normalize("NFKD", text)
print("NFKD:", nfkd)

# 5. Check Combining Characters
text = "café"
normalized = unicodedata.normalize("NFD", text)
print("\nCombining Characters:")
for char in normalized:
    print(char, unicodedata.combining(char))

# 6. Remove Accents
text = "café résumé naïve"
normalized = unicodedata.normalize("NFD", text)
result = "".join(
    char for char in normalized
    if not unicodedata.combining(char)
)
print("\nWithout Accents:", result)

# 7. Compare Normalized Strings
text1 = "café"
text2 = "cafe\u0301"
print("\nBefore Normalization:", text1 == text2)
text1 = unicodedata.normalize("NFC", text1)
text2 = unicodedata.normalize("NFC", text2)
print("After Normalization:", text1 == text2)