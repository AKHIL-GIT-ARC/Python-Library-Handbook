# Mini Project - Text Encoder / Decoder

text = input("Enter text: ")

print("\n--- Text Encoding ---")

# Encode text
encoded = text.encode("utf-8")
print("Original :", text)
print("Encoded  :", encoded)

# Decode bytes
decoded = encoded.decode("utf-8")
print("Decoded  :", decoded)

# Show size
print("Byte Size:", len(encoded))

# Verify
if text == decoded:
    print("Status   : Encoding and decoding successful")
else:
    print("Status   : Error")