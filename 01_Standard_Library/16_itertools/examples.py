from itertools import count
from itertools import cycle
from itertools import repeat
from itertools import chain
from itertools import compress
from itertools import accumulate
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import zip_longest

print("=" * 30)
print("   itertools Module Examples")
print("=" * 30)


# ==================================================
# count()
# ==================================================

print("\n1. count()")
counter = count(1)
print(next(counter))
print(next(counter))
print(next(counter))


# ==================================================
# cycle()
# ==================================================

print("\n2. cycle()")
colors = cycle(["Red", "Blue"])
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))


# ==================================================
# repeat()
# ==================================================

print("\n3. repeat()")
for value in repeat("Python", 3):
    print(value)


# ==================================================
# chain()
# ==================================================

print("\n4. chain()")
numbers = chain([1, 2], [3, 4], [5, 6])
print(list(numbers))


# ==================================================
# compress()
# ==================================================

print("\n5. compress()")
data = ["Apple", "Banana", "Orange", "Mango"]
selectors = [1, 0, 1, 0]
print(list(compress(data, selectors)))


# ==================================================
# accumulate()
# ==================================================

print("\n6. accumulate()")
numbers = [10, 20, 30, 40]
print(list(accumulate(numbers)))


# ==================================================
# product()
# ==================================================

print("\n7. product()")
colors = ["Red", "Blue"]
sizes = ["S", "M"]
print(list(product(colors, sizes)))


# ==================================================
# permutations()
# ==================================================

print("\n8. permutations()")
letters = ["A", "B", "C"]
print(list(permutations(letters, 2)))


# ==================================================
# combinations()
# ==================================================

print("\n9. combinations()")
numbers = [1, 2, 3, 4]
print(list(combinations(numbers, 2)))


# ==================================================
# combinations_with_replacement()
# ==================================================

print("\n10. combinations_with_replacement()")
print(list(combinations_with_replacement(["A", "B"], 2)))


# ==================================================
# zip_longest()
# ==================================================

print("\n11. zip_longest()")
names = ["Akhil", "Charan", "Om"]
marks = [90, 99]
print(list(zip_longest(names, marks, fillvalue="N/A")))


# ==================================================
# Summary
# ==================================================

print("\n" + "=" * 10)
print(" Summary")
print("=" * 10)
print("count()                          -> Infinite counting")
print("cycle()                          -> Repeat iterable")
print("repeat()                         -> Repeat value")
print("chain()                          -> Merge iterables")
print("compress()                       -> Filter using selectors")
print("accumulate()                     -> Running totals")
print("product()                        -> Cartesian product")
print("permutations()                   -> Ordered arrangements")
print("combinations()                   -> Unordered selections")
print("combinations_with_replacement()  -> Combinations with repeats")
print("zip_longest()                    -> Zip unequal iterables")