# Calendar Module Cheat Sheet

## Import

```python
import calendar
```

The `calendar` module is used to display calendars, check leap years, determine weekdays, and perform calendar-related operations.

---

## 1. calendar.calendar()

**Purpose:** Displays the calendar for an entire year.

**Syntax**

```python
calendar.calendar(year)
```

**Parameters:** `year (int)`

**Returns:** `str`

**Example**

```python
print(calendar.calendar(2026))
```

**Real-world Uses**
- Annual planners
- School calendars
- Event scheduling

> 💡 **Interview Tip:** Returns the calendar as a string.

---

## 2. calendar.month()

**Purpose:** Displays the calendar for a specific month.

**Syntax**

```python
calendar.month(year, month)
```

**Parameters:**
- `year`
- `month`

**Returns:** `str`

**Example**

```python
print(calendar.month(2026, 7))
```

**Real-world Uses**
- Booking systems
- Attendance systems
- Monthly planners

---

## 3. calendar.weekday()

**Purpose:** Returns the weekday index for a given date.

**Syntax**

```python
calendar.weekday(year, month, day)
```

**Returns:** `int`

| Value | Day |
|------:|------|
| 0 | Monday |
| 1 | Tuesday |
| 2 | Wednesday |
| 3 | Thursday |
| 4 | Friday |
| 5 | Saturday |
| 6 | Sunday |

**Example**

```python
day = calendar.weekday(2026, 7, 8)
print(calendar.day_name[day])
```

---

## 4. calendar.isleap()

**Purpose:** Checks whether a year is a leap year.

**Syntax**

```python
calendar.isleap(year)
```

**Returns:** `bool`

**Example**

```python
calendar.isleap(2024)
```

**Output**

```
True
```

**Real-world Uses**
- Age calculation
- Date validation
- Payroll systems

---

## 5. calendar.leapdays()

**Purpose:** Counts leap years between two years.

**Syntax**

```python
calendar.leapdays(start, end)
```

**Example**

```python
calendar.leapdays(2000, 2026)
```

**Returns**

```
7
```

---

## 6. calendar.monthrange()

**Purpose:** Returns the first weekday and total number of days in a month.

**Syntax**

```python
calendar.monthrange(year, month)
```

**Returns**

```python
(first_weekday, total_days)
```

**Example**

```python
first, days = calendar.monthrange(2026, 7)
```

---

## 7. calendar.monthcalendar()

**Purpose:** Returns a month's calendar as a nested list.

**Syntax**

```python
calendar.monthcalendar(year, month)
```

**Example**

```python
print(calendar.monthcalendar(2026, 7))
```

**Real-world Uses**
- Calendar UIs
- Scheduling applications

---

## 8. calendar.day_name

**Purpose:** Returns all weekday names.

**Example**

```python
for day in calendar.day_name:
    print(day)
```

---

## 9. calendar.month_name

**Purpose:** Returns all month names.

**Example**

```python
for month in calendar.month_name[1:]:
    print(month)
```

---

# Comparison

## calendar.month() vs calendar.calendar()

| calendar.month() | calendar.calendar() |
|------------------|---------------------|
| One month | Entire year |

---

## isleap() vs leapdays()

| isleap() | leapdays() |
|-----------|------------|
| Checks one year | Counts leap years |

---

## Frequently Used Functions

| Function | Purpose |
|----------|---------|
| `calendar()` | Year calendar |
| `month()` | Monthly calendar |
| `weekday()` | Find weekday |
| `isleap()` | Check leap year |
| `leapdays()` | Count leap years |
| `monthrange()` | First weekday & total days |
| `monthcalendar()` | Calendar matrix |
| `day_name` | Weekday names |
| `month_name` | Month names |

---

# Best Practices

- Use `month()` for displaying a monthly calendar.
- Use `weekday()` to determine the day of a date.
- Use `monthrange()` to find the number of days in a month.
- Use `isleap()` before handling February.

---

# Common Mistakes

- Using month values outside **1–12**.
- Confusing `calendar` with `datetime`.
- Forgetting that `weekday()` starts from **Monday = 0**.

---

# When Should I Use This Module?

✅ **Use `calendar` when:**

- Displaying calendars
- Checking leap years
- Finding weekdays
- Scheduling events

❌ **Avoid `calendar` when:**

- Performing date arithmetic
- Calculating age
- Measuring time

➡ **Better Alternatives**

- `datetime` → Date calculations
- `time` → Time operations

---

# Quick Revision

| Need | Function |
|------|----------|
| Year Calendar | `calendar()` |
| Monthly Calendar | `month()` |
| Find Weekday | `weekday()` |
| Check Leap Year | `isleap()` |
| Count Leap Years | `leapdays()` |
| Days in Month | `monthrange()` |
| Calendar Matrix | `monthcalendar()` |
| Weekday Names | `day_name` |
| Month Names | `month_name` |