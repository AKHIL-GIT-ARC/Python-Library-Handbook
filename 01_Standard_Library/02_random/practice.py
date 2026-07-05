import random

# Question 1
print("Random Integer:", random.randint(1, 100))

# Question 2
colors = ["Red", "Blue", "Green", "Yellow"]
print("Random Color:", random.choice(colors))

# Question 3
numbers = list(range(1, 11))
random.shuffle(numbers)
print("Shuffled List:", numbers)

# Question 4
students = ["Akhil", "Om", "Sai", "Priya", "Charan"]
print("Random Student:", random.choice(students))

# Question 5
print("Lottery Numbers:", random.sample(range(1, 50), 6))