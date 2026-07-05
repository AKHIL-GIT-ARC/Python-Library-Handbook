import random
import string
def dice_roller():
    print(f"\nDice Rolled: {random.randint(1, 6)}")


def coin_toss():
    print(f"\nCoin Toss: {random.choice(['Heads','Tails'])}")


def password_generator():
    length = int(input("\nEnter password length: "))

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = "".join(random.choices(characters, k=length))

    print(f"\nGenerated Password: {password}")


def lottery_generator():
    numbers = random.sample(range(1, 50), 6)
    numbers.sort()

    print("\nLottery Numbers:", numbers)


def random_student():
    students = [
        "Akhil",
        "Charan",
        "Priya",
        "Sai",
        "Om",
        "Kiran",
        "Meghana"
    ]

    print(f"\n Selected Student: {random.choice(students)}")


def random_teams():
    students = [
        "Akhil",
        "Charan",
        "Priya",
        "Sai",
        "Om",
        "Kiran",
        "Meghana"
    ]
    random.shuffle(students)
    midpoint = len(students) // 2
    team_a = students[:midpoint]
    team_b = students[midpoint:]
    print("\nTeam A")
    print(team_a)
    print("\nTeam B")
    print(team_b)


def random_float():
    number = random.uniform(1, 100)
    print(f"\n Random Decimal Number: {number:.2f}")


while True:
    print("\n" + "=" * 45)
    print("         RANDOM UTILITY TOOLKIT")
    print("=" * 45)
    print("1. Dice Roller")
    print("2. Coin Toss")
    print("3. Password Generator")
    print("4. Lottery Number Generator")
    print("5. Random Student Picker")
    print("6. Random Team Generator")
    print("7. Random Decimal Number")
    print("8. Exit")

    choice = input("\nEnter your choice: ")
    if choice == "1":
        dice_roller()
    elif choice == "2":
        coin_toss()
    elif choice == "3":
        password_generator()
    elif choice == "4":
        lottery_generator()
    elif choice == "5":
        random_student()
    elif choice == "6":
        random_teams()
    elif choice == "7":
        random_float()
    elif choice == "8":
        print("\nThank you for using the Random Utility Toolkit!")
        break
    else:
        print("\nInvalid Choice! Please try again.")