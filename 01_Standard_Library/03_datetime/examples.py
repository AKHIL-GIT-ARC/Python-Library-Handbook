"""
===========================================
Datetime Module - Examples
===========================================

This file demonstrates the most commonly used
functions of Python's built-in datetime module.
"""

# -----------------------------------------
# Importing the Module
# -----------------------------------------

from datetime import datetime, date, time, timedelta


# -----------------------------------------
# 1. Current Date and Time
# -----------------------------------------

print("\n========== Current Date & Time ==========")
current_datetime = datetime.now()
print("Current Date & Time:", current_datetime)


# -----------------------------------------
# 2. Current Date
# -----------------------------------------

print("\n========== Current Date ==========")
today = date.today()
print("Today's Date:", today)


# -----------------------------------------
# 3. Access Individual Components
# -----------------------------------------

print("\n========== Date Components ==========")

print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)

print("\n========== Time Components ==========")

print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)


# -----------------------------------------
# 4. Create Custom Date
# -----------------------------------------

print("\n========== Custom Date ==========")
birthday = date(2005, 7, 18)
print("Birthday:", birthday)


# -----------------------------------------
# 5. Create Custom Time
# -----------------------------------------

print("\n========== Custom Time ==========")
alarm = time(6, 30, 0)
print("Alarm Time:", alarm)


# -----------------------------------------
# 6. Formatting Dates
# -----------------------------------------

print("\n========== strftime() ==========")

print("DD/MM/YYYY :", current_datetime.strftime("%d/%m/%Y"))
print("Month Name :", current_datetime.strftime("%B"))
print("Day Name   :", current_datetime.strftime("%A"))
print("Time       :", current_datetime.strftime("%I:%M:%S %p"))


# -----------------------------------------
# 7. Convert String to Date
# -----------------------------------------

print("\n========== strptime() ==========")

date_string = "15-08-2026"
converted_date = datetime.strptime(date_string, "%d-%m-%Y")
print("Converted Date:", converted_date)


# -----------------------------------------
# 8. Date Arithmetic
# -----------------------------------------

print("\n========== timedelta() ==========")

today = datetime.now()
future = today + timedelta(days=30)
past = today - timedelta(days=30)
print("Today :", today)
print("30 Days Later :", future)
print("30 Days Earlier :", past)


# -----------------------------------------
# 9. Difference Between Dates
# -----------------------------------------

print("\n========== Difference Between Dates ==========")

start = datetime(2026, 1, 1)
end = datetime(2026, 12, 31)
difference = end - start
print("Difference:", difference.days, "days")


# -----------------------------------------
# 10. Compare Dates
# -----------------------------------------

print("\n========== Date Comparison ==========")

date1 = datetime(2026, 5, 1)
date2 = datetime(2026, 10, 1)
print("date1 < date2 :", date1 < date2)
print("date1 > date2 :", date1 > date2)
print("date1 == date2:", date1 == date2)


# -----------------------------------------
# 11. Replace Date Components
# -----------------------------------------

print("\n========== replace() ==========")

current = datetime.now()
modified = current.replace(year=2030)
print("Current :", current)
print("Modified:", modified)


# -----------------------------------------
# 12. Timestamp
# -----------------------------------------

print("\n========== timestamp() ==========")

print("Timestamp:", current.timestamp())


# -----------------------------------------
# 13. Weekday
# -----------------------------------------

print("\n========== weekday() ==========")

print("weekday():", current.weekday())
print("isoweekday():", current.isoweekday())


# -----------------------------------------
# 14. Combine Date and Time
# -----------------------------------------

print("\n========== combine() ==========")

custom_date = date(2026, 7, 10)
custom_time = time(10, 45)

combined = datetime.combine(custom_date, custom_time)

print(combined)
