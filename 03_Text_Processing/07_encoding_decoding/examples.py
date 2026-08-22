# Encoding and Decoding - Examples

# 1. Encoding

text = "Hello"
data = text.encode("utf-8")
print("Original:", text)
print("Encoded :", data)

# 2. Decoding
decoded = data.decode("utf-8")
print("\nDecoded:", decoded)

# 3. Encoding Unicode Text
text = "Hello ₹ 😀"
encoded = text.encode("utf-8")
print("\nUnicode Text:", text)
print("Encoded:", encoded)

# 4. Decode Unicode Bytes
decoded = encoded.decode("utf-8")
print("Decoded:", decoded)

# 5. str vs bytes
print("\nTypes:")
print(type(text))
print(type(encoded))

# 6. Different Encodings
text = "Python"
print("\nDifferent Encodings:")
print("UTF-8 :", text.encode("utf-8"))
print("UTF-16:", text.encode("utf-16"))

# 7. Encoding Error
text = "₹"
try:
    print(text.encode("ascii"))
except UnicodeEncodeError:
    print("\nASCII cannot encode ₹")

# 8. errors="ignore"
text = "Hello ₹"
print("\nIgnore Error:")
print(text.encode("ascii", errors="ignore"))

# 9. errors="replace"
print("\nReplace Error:")
print(text.encode("ascii", errors="replace"))

# 10. Complete Encoding → Decoding Flow
text = "Python ₹"
encoded = text.encode("utf-8")
decoded = encoded.decode("utf-8")
print("\nComplete Flow:")
print("Original :", text)
print("Encoded  :", encoded)
print("Decoded  :", decoded)