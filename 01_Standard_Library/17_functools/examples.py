"""
examples.py
Module: functools
"""
from functools import (
    partial,
    reduce,
    lru_cache,
    wraps,
    cmp_to_key,
    cached_property,
    total_ordering,
    singledispatch
)
print("=" * 20)
print("1. partial()")
print("=" * 20)
def multiply(a, b):
    return a * b
multiply_by_10 = partial(multiply, b=10)
print(multiply_by_10(5))
print(multiply_by_10(8))
print(multiply_by_10(12))

print("\n" + "=" * 20)
print("2. reduce()")
print("=" * 20)
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
product = reduce(lambda x, y: x * y, numbers)
print("Numbers :", numbers)
print("Sum      :", total)
print("Product  :", product)


print("\n" + "=" * 20)
print("3. lru_cache()")
print("=" * 20)
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print("Fibonacci(10):", fibonacci(10))
print("Fibonacci(15):", fibonacci(15))

print("\n" + "=" * 20)
print("4. wraps()")
print("=" * 20)
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function Started")
        result = func(*args, **kwargs)
        print("Function Finished")
        return result
    return wrapper
@logger
def greet(name):
    print(f"Hello, {name}!")
greet("Akhil")
print("Function Name:", greet.__name__)


print("\n" + "=" * 20)
print("5. cmp_to_key()")
print("=" * 20)
def compare(a, b):
    return a - b
numbers = [5, 1, 9, 3, 7]
numbers.sort(key=cmp_to_key(compare))
print(numbers)


print("\n" + "=" * 20)
print("6. cached_property()")
print("=" * 20)
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @cached_property
    def area(self):
        print("Calculating Area...")
        return 3.14159 * self.radius ** 2
circle = Circle(5)
print(circle.area)
print(circle.area)      # Uses cached value


print("\n" + "=" * 20)
print("7. total_ordering()")
print("=" * 20)
@total_ordering
class Student:
    def __init__(self, marks):
        self.marks = marks
    def __eq__(self, other):
        return self.marks == other.marks
    def __lt__(self, other):
        return self.marks < other.marks
student1 = Student(85)
student2 = Student(92)
print(student1 < student2)
print(student1 <= student2)
print(student1 == student2)
print(student1 > student2)


print("\n" + "=" * 20)
print("8. singledispatch()")
print("=" * 20)
@singledispatch
def display(value):
    print("Unknown Type")
@display.register(int)
def _(value):
    print("Integer :", value)
@display.register(str)
def _(value):
    print("String :", value)
@display.register(list)
def _(value):
    print("List :", value)
display(100)
display("Python")
display([1, 2, 3])
display(3.14)


print("\n" + "=" * 20)
print("Summary")
print("=" * 20)
print("""
✓ partial()                  -> Fix function arguments
✓ reduce()                   -> Reduce iterable to one value
✓ lru_cache()                -> Cache function results
✓ wraps()                    -> Preserve decorator metadata
✓ cmp_to_key()               -> Custom sorting
✓ cached_property()          -> Cache computed property
✓ total_ordering()           -> Auto-generate comparison methods
✓ singledispatch()           -> Generic functions
""")