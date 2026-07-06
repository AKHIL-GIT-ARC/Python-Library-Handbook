# Datetime Module

## Introduction

The `datetime` module is a built-in Python library used for working with dates and times. It allows developers to create, manipulate, compare, format, and calculate dates and times efficiently.

Unlike the `time` module, `datetime` provides object-oriented classes that make date and time operations easier and more readable.

---

# Why Learn This Library?

The `datetime` module is one of the most frequently used Python libraries because almost every application deals with dates or time.

Examples include:

- Login Systems
- Attendance Systems
- Banking Applications
- E-commerce Websites
- Scheduling Applications
- Event Management Systems
- AI & Machine Learning
- Logging
- APIs
- Data Analysis

---

# Features

- Create dates and times
- Format dates into readable strings
- Convert strings into dates
- Calculate date differences
- Add or subtract days
- Compare dates
- Work with timestamps
- Handle time zones

---

# Installation

The `datetime` module is included with Python.

No installation is required.

---

# Import

```python
from datetime import datetime
```

or

```python
import datetime
```

---

# Important Classes

The datetime module provides several useful classes.

| Class | Purpose |
|--------|----------|
| datetime | Represents both date and time |
| date | Represents only the date |
| time | Represents only the time |
| timedelta | Represents a duration between dates |
| timezone | Handles timezone information |

---

# Important Functions

We'll learn:

- datetime.now()
- datetime.today()
- date.today()
- datetime.strptime()
- datetime.strftime()
- timedelta()
- replace()
- combine()
- timestamp()
- weekday()
- isoweekday()

---

# Real-world Applications

The datetime module is used in:

- Attendance Management Systems
- Employee Payroll
- Banking Software
- Hospital Management Systems
- Hotel Booking Systems
- Online Shopping
- Event Scheduling
- Data Logging
- AI Model Timestamping

---

# Advantages

- Easy date calculations
- Powerful formatting options
- Built-in support
- Supports time arithmetic
- Supports time zones

---

# Limitations

- Timezone handling can become complex.
- Leap seconds are not supported.
- Beginners often confuse datetime, date, and time objects.

---

# Best Practices

- Use `datetime.now()` for the current date and time.
- Use `strftime()` for formatting dates.
- Use `strptime()` to convert strings into datetime objects.
- Use `timedelta` for adding or subtracting dates.
- Store dates in ISO format whenever possible.

---

# Common Mistakes

- Forgetting to import datetime correctly.
- Mixing `date` and `datetime` objects.
- Incorrect format strings in `strftime()` and `strptime()`.
- Comparing formatted strings instead of datetime objects.

---

# Mini Project

========================================
      DATE & AGE UTILITY TOOLKIT
========================================

1. Current Date & Time
2. Calculate Age
3. Days Between Two Dates
4. Find Day of the Week
5. Add Days to a Date
6. Exit

It demonstrates:
datetime.now()
strptime()
strftime()
timedelta()
Date arithmetic
User input
Functions
Loops
Conditionals

---

# References

Official Python Documentation

https://docs.python.org/3/library/datetime.html