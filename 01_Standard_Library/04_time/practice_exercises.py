import time
import random

print("===== Time Module Practice =====")

# ---------------------------------------
# 1. Print Current Unix Timestamp
# ---------------------------------------

print("\n1. Current Unix Timestamp")
timestamp = time.time()
print(timestamp)

# ---------------------------------------
# 2. Print Current Local Time
# ---------------------------------------

print("\n2. Current Local Time")
print(time.ctime())

# ---------------------------------------
# 3. Display Local and UTC Time
# ---------------------------------------

print("\n3. Local vs UTC")
print("Local :", time.strftime("%d-%m-%Y %I:%M:%S %p", time.localtime()))
print("UTC   :", time.strftime("%d-%m-%Y %I:%M:%S %p", time.gmtime()))

# ---------------------------------------
# 4. Pause Program
# ---------------------------------------

print("\n4. Sleep Function")
print("Waiting for 2 seconds...")
time.sleep(2)
print("Program Resumed")

# ---------------------------------------
# 5. Measure Execution Time
# ---------------------------------------

print("\n5. Measure Execution Time")
numbers = [random.randint(1, 10000) for _ in range(10000)]
start = time.perf_counter()
numbers.sort()
end = time.perf_counter()
print("Sorting Time:", round(end-start, 6), "seconds")

# ---------------------------------------
# 6. Measure CPU Time
# ---------------------------------------

print("\n6. CPU Time")
start = time.process_time()
total = 0
for i in range(1000000):
    total += i
end = time.process_time()
print("CPU Time:", round(end - start, 6), "seconds")

# ---------------------------------------
# 7. Stopwatch
# ---------------------------------------

print("\n7. Stopwatch")
input("Press ENTER to Start...")
start = time.perf_counter()
input("Press ENTER to Stop...")
end = time.perf_counter()
print("Elapsed Time:", round(end - start, 2), "seconds")

# ---------------------------------------
# 8. Countdown Timer
# ---------------------------------------

print("\n8. Countdown Timer")
for second in range(5, 0, -1):
    print(second)
    time.sleep(1)
print("Time's Up!")

# ---------------------------------------
# 9. Current Time Every Second
# ---------------------------------------

print("\n9. Live Clock")
for _ in range(5):
    print(time.strftime("%I:%M:%S %p"))
    time.sleep(1)

# ---------------------------------------
# 10. Measure Sleep Using Monotonic
# ---------------------------------------

print("\n10. Monotonic Timer")
start = time.monotonic()
time.sleep(3)
end = time.monotonic()
print("Elapsed:", round(end - start, 2), "seconds")