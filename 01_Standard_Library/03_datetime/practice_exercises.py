from datetime import datetime, date, time, timedelta

print("===== Datetime Practice =====")

# ---------------------------------------
# 1. Get Current Date & Time
# ---------------------------------------

today = date.today()
now = datetime.now()
print("Today's Date:", today)
print("Current Time:", now)

# ---------------------------------------
# 2. Extract Date Components
# ---------------------------------------

print("\nYear :", now.year)
print("Month:", now.month)
print("Day  :", now.day)

# ---------------------------------------
# 3. Create Custom Date & Time
# ---------------------------------------

birthday = date(2005, 7, 18)
alarm = time(6, 30)
print("\nBirthday:", birthday)
print("Alarm:", alarm)

# ---------------------------------------
# 4. Format Date
# ---------------------------------------

print("\nFormatted Date:")
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%A"))

# ---------------------------------------
# 5. Convert String to Date
# ---------------------------------------

date_str = "25-12-2026"
converted = datetime.strptime(date_str, "%d-%m-%Y")
print("\nConverted:", converted)

# ---------------------------------------
# 6. Date Arithmetic
# ---------------------------------------

print("\nAfter 10 Days :", now + timedelta(days=10))
print("Before 10 Days:", now - timedelta(days=10))

# ---------------------------------------
# 7. Difference Between Dates
# ---------------------------------------

start = datetime(2026, 1, 1)
end = datetime(2026, 12, 31)

print("\nDays:", (end - start).days)

# ---------------------------------------
# 8. Compare Dates
# ---------------------------------------

print("\nComparison:", start < end)

# ---------------------------------------
# 9. Replace Year
# ---------------------------------------

print("\nModified:", now.replace(year=2030))

# ---------------------------------------
# 10. Combine Date & Time
# ---------------------------------------

custom = datetime.combine(
    date(2026, 7, 10),
    time(9, 30)
)
print("\nCombined:", custom)

# ---------------------------------------
# 11. Timestamp
# ---------------------------------------

print("\nTimestamp:", now.timestamp())

# ---------------------------------------
# 12. Calculate Age
# ---------------------------------------

birth = datetime.strptime("12-09-2006", "%d-%m-%Y")
age = now.year - birth.year
if (now.month, now.day) < (birth.month, birth.day):
    age -= 1
print("\nAge:", age)