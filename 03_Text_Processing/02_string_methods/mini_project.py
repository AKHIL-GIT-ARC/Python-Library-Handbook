# Mini Project - Text Analyzer

text = input("Enter a sentence: ")
print("\n----- Text Analysis -----")
print("Original Text :", text)
print("Uppercase     :", text.upper())
print("Lowercase     :", text.lower())
print("Title Case    :", text.title())
print("Length        :", len(text))
print("Word Count    :", len(text.split()))
print("Contains 'Python':", "Python" in text)
print("Starts With 'Python':", text.startswith("Python"))
print("Ends With '.':", text.endswith("."))
print("\nWords:")
for word in text.split():
    print(word)