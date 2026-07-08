# Calendar Module

## Introduction

The `calendar` module is a built-in Python library used to display calendars, determine weekdays, check leap years, and perform calendar-related operations.

It provides an easy way to generate monthly or yearly calendars and retrieve useful date information.

---

## Why Learn This Library?

The `calendar` module is useful when developing applications that involve dates and scheduling.

Common use cases include:

- Calendar Applications
- Event Management Systems
- Booking Systems
- School Timetables
- Attendance Systems
- Scheduling Software

---

## Features

- Display monthly calendars
- Display yearly calendars
- Check leap years
- Find weekdays
- Count leap years
- Find the number of days in a month

---

## Installation

The `calendar` module is built into Python.

No installation is required.

---

## Import

```python
import calendar
```

---

## Important Functions

- calendar.calendar()
- calendar.month()
- calendar.weekday()
- calendar.isleap()
- calendar.leapdays()
- calendar.monthrange()
- calendar.monthcalendar()
- calendar.day_name
- calendar.month_name

---

## Real-world Applications

- Digital Calendars
- Leave Management Systems
- Hotel Booking Systems
- School Management Software
- Employee Attendance
- Appointment Scheduling

---

## Advantages

- Easy to use
- Built into Python
- Supports leap year calculations
- Generates formatted calendars

---

## Limitations

- Limited to calendar-related operations
- Cannot perform advanced date arithmetic (use `datetime`)

---

## Best Practices

- Use `calendar.month()` to display monthly calendars.
- Use `calendar.isleap()` before working with February.
- Use `calendar.weekday()` to determine the day of a specific date.
- Use `datetime` when performing date calculations.

---

## Common Mistakes

- Confusing `calendar` with `datetime`
- Forgetting that months range from 1–12
- Passing invalid dates to `weekday()`

---

## Mini Project

### Calendar Utility

Features:

- Display Monthly Calendar
- Display Year Calendar
- Check Leap Year
- Find Weekday
- Find Days in a Month

---

## References

Official Python Documentation

https://docs.python.org/3/library/calendar.html