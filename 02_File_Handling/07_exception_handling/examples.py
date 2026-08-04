# Exception Handling - Examples

# -------------------------------
# 1. try - except
# -------------------------------
print("1. try - except")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")


# -------------------------------
# 2. Handling ValueError
# -------------------------------
print("\n2. ValueError")
try:
    number = int(input("Enter a number: "))
    print("Number:", number)
except ValueError:
    print("Please enter a valid integer.")


# -------------------------------
# 3. Multiple Exceptions
# -------------------------------
print("\n3. Multiple Exceptions")
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")


# -------------------------------
# 4. else
# -------------------------------
print("\n4. else")
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", number)


# -------------------------------
# 5. finally
# -------------------------------
print("\n5. finally")
try:
    print("Program started.")
finally:
    print("Program ended.")


# -------------------------------
# 6. raise
# -------------------------------
print("\n6. raise")
try:
    age = 16
    if age < 18:
        raise ValueError("Age must be 18 or above.")
except ValueError as error:
    print(error)


# -------------------------------
# 7. FileNotFoundError
# -------------------------------
print("\n7. FileNotFoundError")
try:
    with open("sample.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")


# -------------------------------
# 8. IndexError
# -------------------------------
print("\n8. IndexError")
numbers = [10, 20, 30]
try:
    print(numbers[5])
except IndexError:
    print("Index out of range.")


# -------------------------------
# 9. KeyError
# -------------------------------
print("\n9. KeyError")
student = {
    "name": "Akhil",
    "age": 20
}
try:
    print(student["marks"])
except KeyError:
    print("Key not found.")