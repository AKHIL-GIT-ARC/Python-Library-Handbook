# String Formatting - Examples

# 1. % Formatting
name = "Akhil"
age = 20
print("Name: %s, Age: %d" % (name, age))


# 2. str.format()
print("Name: {}, Age: {}".format(name, age))
print("Name: {name}, Age: {age}".format(
    name=name,
    age=age
))


# 3. f-Strings ⭐
print(f"Name: {name}, Age: {age}")
a = 10
b = 20
print(f"Total: {a + b}")


# 4. Decimal Precision
price = 99.5678
print(f"Price: ₹{price:.2f}")


# 5. Number Formatting
number = 1000000
print(f"Number: {number:,}")


# 6. Percentage
score = 0.875
print(f"Score: {score:.1%}")


# 7. Alignment
language = "Python"
print(f"Left:   |{language:<10}|")
print(f"Right:  |{language:>10}|")
print(f"Center: |{language:^10}|")


# 8. Width
print(f"|{language:10}|")


# 9. Combining Format Specifiers
amount = 1234567.891
print(f"Amount: ₹{amount:,.2f}")


# 10. Expressions in f-strings
x = 15
y = 5
print(f"{x} + {y} = {x + y}")
print(f"{x} × {y} = {x * y}")