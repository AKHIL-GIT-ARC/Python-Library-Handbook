# Calendar Module Interview Questions

## Beginner Level

### 1. What is the `calendar` module?

**Answer:**  
The `calendar` module is a built-in Python library used to display calendars, check leap years, find weekdays, and perform calendar-related operations.

---

### 2. How do you import the `calendar` module?

```python
import calendar
```

---

### 3. Which function displays a month's calendar?

**Answer:**

```python
calendar.month(year, month)
```

---

### 4. Which function displays an entire year's calendar?

**Answer:**

```python
calendar.calendar(year)
```

---

### 5. How do you check if a year is a leap year?

**Answer:**

```python
calendar.isleap(2024)
```

Returns `True` if it's a leap year; otherwise `False`.

---

## Intermediate Level

### 6. What does `calendar.weekday()` return?

**Answer:**  
It returns the weekday index (0–6) for a given date.

```python
calendar.weekday(2026, 7, 8)
```

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

### 7. What is the purpose of `calendar.monthrange()`?

**Answer:**  
It returns the first weekday and the total number of days in a month.

```python
calendar.monthrange(2026, 7)
```

Returns:

```python
(2, 31)
```

---

### 8. What does `calendar.monthcalendar()` return?

**Answer:**  
It returns a nested list representing the month's calendar.

Example:

```python
calendar.monthcalendar(2026, 7)
```

---

### 9. What is `calendar.leapdays()`?

**Answer:**  
It counts the number of leap years within a given range.

```python
calendar.leapdays(2000, 2026)
```

---

### 10. How do you print all month names?

**Answer:**

```python
for month in calendar.month_name[1:]:
    print(month)
```

---

## Advanced Level

### 11. Difference between `calendar()` and `month()`?

| `calendar()` | `month()` |
|--------------|-----------|
| Displays a full year | Displays a single month |

---

### 12. Difference between `isleap()` and `leapdays()`?

| `isleap()` | `leapdays()` |
|-------------|--------------|
| Checks one year | Counts leap years in a range |

---

### 13. What is the difference between `calendar` and `datetime`?

| `calendar` | `datetime` |
|------------|------------|
| Displays calendars | Performs date/time calculations |
| Checks leap years | Date arithmetic |
| Finds weekdays | Calculates date differences |

---

### 14. What happens if you pass an invalid month?

**Answer:**  
Python raises an exception because valid months range from **1 to 12**.

---

### 15. Can the `calendar` module calculate age?

**Answer:**  
No. Use the `datetime` module for age and date calculations.

---

## Scenario-Based Questions

### 16. You need to display a calendar for December 2026. Which function will you use?

**Answer:**

```python
calendar.month(2026, 12)
```

---

### 17. You are building an attendance system. Which function helps determine the weekday of a date?

**Answer:**

```python
calendar.weekday()
```

---

### 18. You need to know how many days February has in 2028. Which function will you use?

**Answer:**

```python
calendar.monthrange(2028, 2)
```

---

### 19. A booking system needs to verify whether a year is a leap year. Which function is most suitable?

**Answer:**

```python
calendar.isleap()
```

---

# Quick Revision

## Frequently Used Functions

| Function | Purpose |
|----------|---------|
| `calendar()` | Display yearly calendar |
| `month()` | Display monthly calendar |
| `weekday()` | Find weekday |
| `isleap()` | Check leap year |
| `leapdays()` | Count leap years |
| `monthrange()` | First weekday & total days |
| `monthcalendar()` | Calendar matrix |
| `day_name` | Weekday names |
| `month_name` | Month names |