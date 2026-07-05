import random

print("----- random() -----")
print(random.random())

print("\n----- randint() -----")
print(random.randint(1, 10))

print("\n----- randrange() -----")
print(random.randrange(1, 20, 2))

print("\n----- uniform() -----")
print(random.uniform(1, 10))

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("\n----- choice() -----")
print(random.choice(fruits))

print("\n----- choices() -----")
print(random.choices(fruits, k=3))

print("\n----- sample() -----")
print(random.sample(fruits, 3))

numbers = [1, 2, 3, 4, 5]

print("\nBefore Shuffle:", numbers)
random.shuffle(numbers)
print("After Shuffle:", numbers)

print("\n----- seed() -----")
random.seed(10)
print(random.randint(1, 100))

print("\n----- getrandbits() -----")
print(random.getrandbits(8))