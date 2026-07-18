from collections import Counter
from collections import defaultdict
from collections import deque
from collections import namedtuple
from collections import OrderedDict
from collections import ChainMap

print("=" * 30)
print(" collections Module Examples")
print("=" * 30)


# ==================================================
# Counter
# ==================================================

print("\n1. Counter")
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = Counter(fruits)
print(counter)
print(counter["apple"])
print(counter.most_common(2))


# ==================================================
# defaultdict
# ==================================================

print("\n2. defaultdict")
marks = defaultdict(int)
marks["Math"] += 95
marks["Science"] += 88
print(marks)
print(marks["English"])      # Missing key returns 0

students = defaultdict(list)
students["CSE"].append("Akhil")
students["CSE"].append("Rahul")
students["AI"].append("Priya")
print(students)


# ==================================================
# deque
# ==================================================

print("\n3. deque")
queue = deque([10, 20, 30])
print(queue)
queue.append(40)
print("After append:", queue)
queue.appendleft(5)
print("After appendleft:", queue)
queue.pop()
print("After pop:", queue)
queue.popleft()
print("After popleft:", queue)


# ==================================================
# namedtuple
# ==================================================

print("\n4. namedtuple")
Student = namedtuple("Student", ["name", "age", "course"])
student = Student("Akhil", 20, "CSE")
print(student)
print(student.name)
print(student.age)
print(student.course)


# ==================================================
# OrderedDict
# ==================================================

print("\n5. OrderedDict")
data = OrderedDict()
data["Python"] = 95
data["Java"] = 88
data["C++"] = 91
print(data)
data.move_to_end("Python")
print(data)


# ==================================================
# ChainMap
# ==================================================

print("\n6. ChainMap")
semester1 = {
    "Math": 90,
    "English": 85
}
semester2 = {
    "Python": 96,
    "AI": 92
}
combined = ChainMap(semester1, semester2)
print(combined)
print(combined["Math"])
print(combined["Python"])


# ==================================================
# Summary
# ==================================================

print("\n" + "=" * 15)
print("    Summary")
print("=" * 15)
print("Counter      -> Count occurrences")
print("defaultdict  -> Default values for missing keys")
print("deque        -> Fast queue and stack")
print("namedtuple   -> Tuple with named fields")
print("OrderedDict  -> Ordered dictionary operations")
print("ChainMap     -> Combine multiple dictionaries")