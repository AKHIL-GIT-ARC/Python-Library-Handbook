# Datetime Module Interview Questions

## Beginner Level

### 1. What is the `datetime` module?

**Answer:**  
The `datetime` module is a built-in Python library used to work with dates, times, and date-time calculations.

---

### 2. What is the difference between `date`, `time`, and `datetime`?

| Class | Purpose |
|--------|---------|
| `date` | Stores only date (YYYY-MM-DD) |
| `time` | Stores only time (HH:MM:SS) |
| `datetime` | Stores both date and time |

---

### 3. How do you get the current date and time?

```python
from datetime import datetime

print(datetime.now())
```

---

### 4. How do you get today's date only?

```python
from datetime import date

print(date.today())
```

---

### 5. What is `timedelta`?

**Answer:**  
`timedelta` represents the difference between two dates or times and is used to add or subtract time.

---

## Intermediate Level

### 6. Difference between `datetime.now()` and `datetime.today()`?

Both return the current local date and time.

`datetime.now()` is generally preferred because it supports timezone arguments.

---

### 7. Difference between `strftime()` and `strptime()`?

| Function | Purpose |
|----------|---------|
| `strftime()` | Datetime → String |
| `strptime()` | String → Datetime |

---

### 8. How do you format a date?

```python
now.strftime("%d/%m/%Y")
```

---

### 9. How do you convert a string into a datetime object?

```python
datetime.strptime("25-12-2026", "%d-%m-%Y")
```

---

### 10. How do you calculate the difference between two dates?

```python
difference = date2 - date1

print(difference.days)
```

---

### 11. How do you add 30 days to today's date?

```python
future = datetime.now() + timedelta(days=30)
```

---

### 12. How do you subtract days from a date?

```python
past = datetime.now() - timedelta(days=15)
```

---

## Advanced Level

### 13. What is a Unix Timestamp?

**Answer:**  
A Unix Timestamp is the number of seconds elapsed since **1 January 1970 (UTC)**.

Example:

```python
datetime.now().timestamp()
```

---

### 14. What does `replace()` do?

It creates a new datetime object with specified values replaced.

```python
now.replace(year=2030)
```

---

### 15. What is `combine()`?

It combines a `date` object and a `time` object into a single `datetime` object.

```python
datetime.combine(date_obj, time_obj)
```

---

### 16. Difference between `weekday()` and `isoweekday()`?

| Method | Monday | Sunday |
|---------|--------|--------|
| `weekday()` | 0 | 6 |
| `isoweekday()` | 1 | 7 |

---

## Scenario-Based Questions

### 17. A user enters their birthday. Which datetime function would you use to calculate their age?

**Answer:**  
Use `datetime.strptime()` to convert the input into a datetime object and compare it with `datetime.today()`.

---

### 18. How would you calculate the number of days remaining until an event?

**Answer:**  
Subtract today's date from the event date using `timedelta`.

---

### 19. A user enters a date as text. Which function converts it into a datetime object?

**Answer:**

```python
datetime.strptime()
```

---

### 20. Which datetime methods did we use in our mini project?

- `datetime.now()`
- `datetime.today()`
- `strptime()`
- `strftime()`
- `timedelta()`

---

# Quick Revision

### Important Classes

- `datetime`
- `date`
- `time`
- `timedelta`

### Important Methods

- `now()`
- `today()`
- `strftime()`
- `strptime()`
- `replace()`
- `combine()`
- `timestamp()`
- `weekday()`
- `isoweekday()`