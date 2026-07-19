from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import accumulate
from itertools import chain
from itertools import zip_longest

def product_combinations():
    colors = ["Red", "Blue"]
    sizes = ["S", "M", "L"]
    print("\nProduct Combinations\n")
    for item in product(colors, sizes):
        print(item)

def password_permutations():
    letters = input("Enter characters (without spaces): ")
    length = int(input("Permutation Length: "))
    print("\nPossible Passwords\n")
    for password in permutations(letters, length):
        print("".join(password))

def lottery_combinations():
    numbers = list(range(1, 11))
    print("\nLottery Combinations\n")
    for combo in combinations(numbers, 3):
        print(combo)

def icecream_combinations():
    flavors = ["Vanilla", "Chocolate", "Strawberry"]
    print("\nFlavor Combinations\n")
    for combo in combinations_with_replacement(flavors, 2):
        print(combo)

def running_total():
    sales = [1200, 1500, 900, 1800, 2100]
    print("\nDaily Sales")
    print(sales)
    print("\nRunning Total")
    print(list(accumulate(sales)))

def merge_lists():
    list1 = ["Python", "Java"]
    list2 = ["C++", "JavaScript"]
    list3 = ["SQL", "MongoDB"]
    print("\nMerged List\n")
    print(list(chain(list1, list2, list3)))

def combine_student_marks():
    students = ["Akhil", "Rahul", "Priya", "John"]
    marks = [95, 90]
    print("\nStudent Marks\n")
    for student in zip_longest(students, marks, fillvalue="Absent"):
        print(student)

while True:
    print("\n" + "=" * 20)
    print("   ITERATOR TOOLKIT")
    print("=" * 20)
    print("1. Product Combinations")
    print("2. Password Permutations")
    print("3. Lottery Combinations")
    print("4. Ice Cream Combinations")
    print("5. Running Sales Total")
    print("6. Merge Multiple Lists")
    print("7. Combine Student Marks")
    print("8. Exit")

    choice = input("\nEnter Choice: ")
    if choice == "1":
        product_combinations()
    elif choice == "2":
        password_permutations()
    elif choice == "3":
        lottery_combinations()
    elif choice == "4":
        icecream_combinations()
    elif choice == "5":
        running_total()
    elif choice == "6":
        merge_lists()
    elif choice == "7":
        combine_student_marks()
    elif choice == "8":
        print("\nThank You For Using Iterator Toolkit!")
        break
    else:
        print("Invalid Choice!")