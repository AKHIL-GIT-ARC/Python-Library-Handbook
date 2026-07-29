# Time Module Cheat Sheet

## Import

```python
import time
```

The `time` module is used for working with timestamps, delays, execution time, and formatting time.

---

# 1. time.time()

**Purpose:** Returns the current Unix timestamp (seconds since January 1, 1970 UTC).

**Syntax**

```python
time.time()
```

**Parameters**

None

**Returns**

`float` (Unix timestamp)

**Example**

```python
import time

print(time.time())
```

**Possible Output**

```
1751873256.784521
```

**Real-world Uses**

- Store timestamps
- Logging
- Session management
- API requests

**Interview Tip**

Returns seconds as a floating-point number.

---

# 2. time.sleep()

**Purpose:** Pauses the execution of the program for a specified number of seconds.

**Syntax**

```python
time.sleep(seconds)
```

**Parameters**

- `seconds` → Number of seconds to pause.

**Returns**

None

**Example**

```python
print("Start")
time.sleep(3)
print("End")
```

**Output**

```
Start
(wait 3 seconds)
End
```

**Real-world Uses**

- Countdown timers
- Retry mechanisms
- Automation scripts

**Important Note**

`sleep()` blocks the current thread while waiting.

---

# 3. time.ctime()

**Purpose:** Converts a Unix timestamp into a readable date and time string.

**Syntax**

```python
time.ctime(timestamp)
```

If no timestamp is provided, it uses the current time.

**Example**

```python
print(time.ctime())
```

**Possible Output**

```
Mon Jul 07 15:30:45 2026
```

**Real-world Uses**

- Display readable timestamps
- Logs
- Reports

---

# 4. time.localtime()

**Purpose:** Returns the current local time as a `struct_time` object.

**Syntax**

```python
time.localtime()
```

**Returns**

`struct_time`

**Example**

```python
local = time.localtime()

print(local)
```

**Output**

```
time.struct_time(...)
```

**Access Components**

```python
print(local.tm_year)
print(local.tm_mon)
print(local.tm_mday)
```

---

# 5. time.gmtime()

**Purpose:** Returns the current UTC (Greenwich Mean Time) as a `struct_time` object.

**Syntax**

```python
time.gmtime()
```

**Example**

```python
print(time.gmtime())
```

**Use Cases**

- Global applications
- Servers
- APIs

---

# 6. time.strftime()

**Purpose:** Formats a time object into a readable string.

**Syntax**

```python
time.strftime(format)
```

**Common Format Codes**

| Code | Meaning |
|------|---------|
| `%d` | Day |
| `%m` | Month |
| `%Y` | Year |
| `%H` | Hour (24-hour) |
| `%I` | Hour (12-hour) |
| `%M` | Minute |
| `%S` | Second |
| `%A` | Weekday |
| `%B` | Month Name |
| `%p` | AM/PM |

**Example**

```python
print(time.strftime("%d-%m-%Y"))
print(time.strftime("%I:%M:%S %p"))
```

**Output**

```
07-07-2026
03:45:10 PM
```

**Real-world Uses**

- Reports
- Digital clocks
- Log files

---

# 7. time.perf_counter()

**Purpose:** Measures high-precision elapsed time.

**Syntax**

```python
time.perf_counter()
```

**Example**

```python
start = time.perf_counter()

# Code

end = time.perf_counter()

print(end - start)
```

**Real-world Uses**

- Benchmarking
- Performance testing
- Algorithm comparison

**Interview Tip**

Preferred over `time.time()` for measuring execution time.

---

# 8. time.process_time()

**Purpose:** Returns CPU time consumed by the current process.

**Syntax**

```python
time.process_time()
```

**Example**

```python
start = time.process_time()

# CPU intensive task

end = time.process_time()

print(end - start)
```

**Important Note**

Does **not** include time spent in `sleep()`.

---

# 9. time.monotonic()

**Purpose:** Returns a clock value that always increases and isn't affected by system clock changes.

**Syntax**

```python
time.monotonic()
```

**Example**

```python
start = time.monotonic()

time.sleep(2)

end = time.monotonic()

print(end - start)
```

**Real-world Uses**

- Timers
- Stopwatches
- Timeout calculations

---

# Comparison Tables

## localtime() vs gmtime()

| localtime() | gmtime() |
|--------------|-----------|
| Local timezone | UTC timezone |

---

## perf_counter() vs process_time()

| perf_counter() | process_time() |
|----------------|----------------|
| Measures elapsed (wall-clock) time | Measures CPU execution time |
| Includes waiting/sleep time | Excludes waiting/sleep time |
| Best for benchmarking | Best for CPU usage analysis |

---

## time.time() vs perf_counter()

| time.time() | perf_counter() |
|--------------|----------------|
| Current Unix timestamp | High-precision timer |
| Used for timestamps | Used for benchmarking |

---

# Frequently Used Functions

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

---

# Best Practices

- Use `perf_counter()` for benchmarking.
- Use `sleep()` only when delays are required.
- Use `strftime()` for displaying formatted time.
- Use `localtime()` for local applications.
- Use `gmtime()` for global systems.

---

# Common Mistakes

- Using `time.time()` instead of `perf_counter()` for benchmarking.
- Expecting `process_time()` to include sleep time.
- Confusing local time with UTC time.
- Using `sleep()` in performance-critical applications.
---

# When Should I Use This Module?

✅ Use `time` when:

- Measuring execution time
- Creating delays
- Working with Unix timestamps
- Building stopwatches
- Creating countdown timers

❌ Avoid `time` when:

- Performing date arithmetic
- Calculating ages
- Working with calendars

➡ Better Alternatives:

- `datetime` → Date calculations
- `calendar` → Calendar operations
- `timeit` → Accurate performance benchmarking

---

# Quick Revision

| Need | Function |
|------|----------|
| Current timestamp | `time.time()` |
| Pause execution | `time.sleep()` |
| Readable current time | `time.ctime()` |
| Local time | `time.localtime()` |
| UTC time | `time.gmtime()` |
| Format time | `time.strftime()` |
| Benchmark code | `time.perf_counter()` |
| CPU time | `time.process_time()` |
| Reliable elapsed time | `time.monotonic()` |