# Datetime Module Cheat Sheet

## Import

```python
from datetime import datetime, date, time, timedelta
```

The `datetime` module is used to work with dates and times.

---

## 1. datetime.now()

**Purpose:** Returns the current date and time.

**Syntax**

```python
datetime.now()
```

**Returns:** `datetime` object

**Example**

```python
print(datetime.now())
```

**Output**

```
2026-07-06 16:45:32.145678
```

**Real-world Uses**
- Login systems
- Logging
- Attendance systems

**Interview Tip**
Returns both date and time.

---

## 2. date.today()

**Purpose:** Returns today's date.

**Syntax**

```python
date.today()
```

**Returns:** `date` object

**Example**

```python
print(date.today())
```

**Output**

```
2026-07-06
```

**Real-world Uses**
- Reports
- Scheduling
- Daily records

---

## 3. datetime.today()

**Purpose:** Returns the current local date and time.

**Syntax**

```python
datetime.today()
```

**Example**

```python
print(datetime.today())
```

**Note**
Very similar to `datetime.now()`.

---

## 4. strftime()

**Purpose:** Converts a datetime object into a formatted string.

**Syntax**

```python
datetime.strftime(format)
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
now.strftime("%d/%m/%Y")
```

**Output**

```
06/07/2026
```

**Real-world Uses**
- Reports
- Bills
- Receipts

---

## 5. strptime()

**Purpose:** Converts a string into a datetime object.

**Syntax**

```python
datetime.strptime(date_string, format)
```

**Example**

```python
datetime.strptime("25-12-2026", "%d-%m-%Y")
```

**Output**

```
2026-12-25 00:00:00
```

**Interview Tip**

- `strftime()` → Datetime → String
- `strptime()` → String → Datetime

---

## 6. timedelta()

**Purpose:** Represents the difference between dates or times.

**Syntax**

```python
timedelta(days=10)
```

**Example**

```python
future = datetime.now() + timedelta(days=10)
```

**Common Parameters**
- days
- weeks
- hours
- minutes
- seconds

**Real-world Uses**
- Subscription expiry
- Booking systems
- Deadlines

---

## 7. replace()

**Purpose:** Replaces one or more components of a date or time.

**Syntax**

```python
replace(year=2030)
```

**Example**

```python
datetime.now().replace(year=2030)
```

---

## 8. combine()

**Purpose:** Combines a `date` and a `time` into one `datetime`.

**Syntax**

```python
datetime.combine(date, time)
```

**Example**

```python
datetime.combine(date(2026,7,10), time(9,30))
```

---

## 9. timestamp()

**Purpose:** Returns the Unix timestamp.

**Syntax**

```python
datetime.now().timestamp()
```

**Real-world Uses**
- APIs
- Databases
- Logging

---

## 10. weekday()

**Purpose:** Returns the weekday number (Monday = 0).

| Value | Day |
|------:|------|
| 0 | Monday |
| 1 | Tuesday |
| 2 | Wednesday |
| 3 | Thursday |
| 4 | Friday |
| 5 | Saturday |
| 6 | Sunday |

---

## 11. isoweekday()

**Purpose:** Returns the weekday number using ISO standard (Monday = 1).

| Value | Day |
|------:|------|
| 1 | Monday |
| 2 | Tuesday |
| 3 | Wednesday |
| 4 | Thursday |
| 5 | Friday |
| 6 | Saturday |
| 7 | Sunday |

---

## Frequently Used Methods

| Method | Purpose |
|---------|---------|
| `datetime.now()` | Current date & time |
| `date.today()` | Today's date |
| `strftime()` | Format datetime |
| `strptime()` | Parse string to datetime |
| `timedelta()` | Date arithmetic |
| `replace()` | Modify a date/time |
| `combine()` | Combine date & time |
| `timestamp()` | Unix timestamp |
| `weekday()` | Weekday (0–6) |
| `isoweekday()` | Weekday (1–7) |

---

## Best Practices

- Use `datetime.now()` when you need both date and time.
- Use `date.today()` when only the date is required.
- Use `strftime()` for formatting.
- Use `strptime()` for parsing user input.
- Use `timedelta()` for date calculations.

---

## Common Mistakes

- Comparing date strings instead of datetime objects.
- Using the wrong format string in `strptime()`.
- Mixing `date` and `datetime` objects.

---

## Interview Tips

| Question | Answer |
|----------|--------|
| `datetime.now()` vs `date.today()` | `now()` returns date & time, `today()` returns only the date. |
| `strftime()` vs `strptime()` | `strftime()` formats a datetime into a string, while `strptime()` parses a string into a datetime object. |