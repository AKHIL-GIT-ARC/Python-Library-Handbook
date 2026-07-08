import calendar

print("===== Calendar Module Practice =====")

# ---------------------------------------
# 1. Display Calendar for Your Birth Month
# ---------------------------------------

print("\n1. Birth Month Calendar")
print(calendar.month(2006, 9))

# ---------------------------------------
# 2. Check Leap Years
# ---------------------------------------

print("\n2. Leap Year Check")
years = [2020, 2024, 2025, 2028]
for year in years:
    print(f"{year}: {calendar.isleap(year)}")

# ---------------------------------------
# 3. Find the Weekday
# ---------------------------------------

print("\n3. Weekday Finder")
weekday = calendar.weekday(2026,7,8)
print(f"{8}-{7}-{2026} is {calendar.day_name[weekday]}")

# ---------------------------------------
# 4. Days in a Month
# ---------------------------------------

print("\n4. Days in a Month")
month = 2
year = 2024
first_day, total_days = calendar.monthrange(year, month)
print("First Day :", calendar.day_name[first_day])
print("Total Days:", total_days)

# ---------------------------------------
# 5. Count Leap Years
# ---------------------------------------

print("\n5. Leap Years Between 2000 and 2050")
print(calendar.leapdays(2000, 2051))

# ---------------------------------------
# 6. Print Month Names
# ---------------------------------------

print("\n6. Month Names")
for month in calendar.month_name[1:]:
    print(month)

# ---------------------------------------
# 7. Print Weekday Names
# ---------------------------------------

print("\n7. Weekday Names")
for day in calendar.day_name:
    print(day)

# ---------------------------------------
# 8. Mini Challenge
# ---------------------------------------

print("\n8. Mini Challenge")
year = int(input("Enter Year: "))
month = int(input("Enter Month (1-12): "))
print(calendar.month(year, month))