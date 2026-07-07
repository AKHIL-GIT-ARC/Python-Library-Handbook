import time

print("===== Time Module Examples =====")

# ---------------------------------------
# 1. Current Unix Timestamp
# ---------------------------------------

print("\n1. Current Timestamp")
print(time.time())

# ---------------------------------------
# 2. Current Local Time
# ---------------------------------------

print("\n2. Current Local Time")
print(time.ctime())

# ---------------------------------------
# 3. Local Time Object
# ---------------------------------------

print("\n3. Local Time Object")
local = time.localtime()
print(local)

# ---------------------------------------
# 4. UTC Time
# ---------------------------------------

print("\n4. UTC Time")
utc = time.gmtime()
print(utc)

# ---------------------------------------
# 5. Formatting Time
# ---------------------------------------

print("\n5. Formatted Time")
print(time.strftime("%d-%m-%Y"))
print(time.strftime("%I:%M:%S %p"))
print(time.strftime("%A"))
print(time.strftime("%B"))

# ---------------------------------------
# 6. Pause Program
# ---------------------------------------

print("\n6. Sleep Function")
print("Wait...")
time.sleep(2)
print("Done!")

# ---------------------------------------
# 7. Measure Execution Time
# ---------------------------------------

print("\n7. Performance Counter")
start = time.perf_counter()
for i in range(1000000):
    pass
end = time.perf_counter()
print("Execution Time:", end - start, "seconds")

# ---------------------------------------
# 8. CPU Process Time
# ---------------------------------------

print("\n8. Process Time")
start = time.process_time()
for i in range(1000000):
    pass
end = time.process_time()
print("CPU Time:", end - start, "seconds")

# ---------------------------------------
# 9. Monotonic Clock
# ---------------------------------------

print("\n9. Monotonic Clock")
start = time.monotonic()
time.sleep(1)
end = time.monotonic()
print("Elapsed Time:", end - start, "seconds")