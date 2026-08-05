# Mini Project - String Analyzer

text = input("Enter a string: ")
print("\n----- String Analysis -----")
print("Original String :", text)
print("Length          :", len(text))
print("First Character :", text[0])
print("Last Character  :", text[-1])
print("Uppercase       :", text.upper())
print("Lowercase       :", text.lower())
print("First 3 Chars   :", text[:3])
print("Last 3 Chars    :", text[-3:])
if "Python" in text:
    print("Contains 'Python': Yes")
else:
    print("Contains 'Python': No")