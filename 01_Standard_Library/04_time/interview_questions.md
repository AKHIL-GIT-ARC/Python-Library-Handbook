# Time Module Interview Questions

## Beginner Level

### 1. What is the `time` module?

**Answer:**
The `time` module is a built-in Python library used for working with time-related operations such as delays, timestamps, execution time measurement, and formatting time.

---

### 2. How do you import the `time` module?

```python
import time
```

---

### 3. What does `time.time()` return?

**Answer:**
It returns the current Unix timestamp, i.e., the number of seconds since January 1, 1970 (UTC).

Example:

```python
time.time()
```

---

### 4. What is the purpose of `time.sleep()`?

**Answer:**
It pauses the execution of the program for the specified number of seconds.

Example:

```python
time.sleep(3)
```

---

### 5. What does `time.ctime()` do?

**Answer:**
It converts a Unix timestamp into a human-readable date and time.

Example:

```python
time.ctime()
```

---

## Intermediate Level

### 6. Difference between `localtime()` and `gmtime()`?

| localtime() | gmtime() |
|-------------|----------|
| Local timezone | UTC timezone |

---

### 7. What does `strftime()` do?

**Answer:**
Formats a time object into a readable string.

Example:

```python
time.strftime("%d-%m-%Y")
```

---

### 8. What is Unix Timestamp?

**Answer:**
A Unix timestamp is the number of seconds elapsed since **1 January 1970 UTC**.

---

### 9. Which function is best for measuring execution time?

**Answer:**

```python
time.perf_counter()
```

It provides the highest available resolution for measuring elapsed time.

---

### 10. What is `process_time()`?

**Answer:**
Returns the CPU time consumed by the current process. It excludes time spent sleeping.

---

### 11. What is `monotonic()`?

**Answer:**
Returns a clock value that always increases and is not affected by system clock changes.

---

### 12. Why is `perf_counter()` preferred over `time.time()` for benchmarking?

**Answer:**
Because `perf_counter()` offers higher precision and is designed specifically for measuring elapsed time.

---

## Advanced Level

### 13. What happens if you call `time.sleep(0)`?

**Answer:**
It doesn't introduce a noticeable delay but may yield execution to other threads depending on the operating system.

---

### 14. Does `time.sleep()` consume CPU while waiting?

**Answer:**
No. The process is suspended and does not actively consume CPU during the sleep period.

---

### 15. What is the difference between wall-clock time and CPU time?

| Wall-clock Time | CPU Time |
|-----------------|----------|
| Total elapsed time | Time the CPU actually spent executing your program |

---

### 16. Which function would you use to benchmark an algorithm?

**Answer:**

```python
time.perf_counter()
```

---

## Scenario-Based Questions

### 17. You are building a countdown timer. Which function is essential?

**Answer:**

```python
time.sleep()
```

---

### 18. You need to measure how long a sorting algorithm takes. Which function should you use?

**Answer:**

```python
time.perf_counter()
```

---

### 19. You want to display the current time in the format `10:45:30 AM`. Which function will you use?

**Answer:**

```python
time.strftime("%I:%M:%S %p")
```

---


# Quick Revision

## Frequently Used Functions

| Function | Purpose |
|----------|---------|
| `time()` | Unix timestamp |
| `sleep()` | Pause execution |
| `ctime()` | Readable current time |
| `localtime()` | Local time object |
| `gmtime()` | UTC time object |
| `strftime()` | Format time |
| `perf_counter()` | Measure execution time |
| `process_time()` | Measure CPU time |
| `monotonic()` | Reliable elapsed time |