import calendar

print("===== Calendar Module Examples =====")

# ---------------------------------------
# 1. Display a Year's Calendar
# ---------------------------------------

print("\n1. Year Calendar (2026)")
print(calendar.calendar(2026))

# ---------------------------------------
# 2. Display a Month's Calendar
# ---------------------------------------

print("\n2. Month Calendar (July 2026)")
print(calendar.month(2026, 7))

# ---------------------------------------
# 3. Find the Weekday
# ---------------------------------------

print("\n3. Weekday")
day = calendar.weekday(2026, 7, 8)
print("Weekday Index:", day)
print("Weekday Name:", calendar.day_name[day])

# ---------------------------------------
# 4. Check Leap Year
# ---------------------------------------

print("\n4. Leap Year")
print("2024:", calendar.isleap(2024))
print("2025:", calendar.isleap(2025))

# ---------------------------------------
# 5. Count Leap Years
# ---------------------------------------

print("\n5. Leap Years Between 2000 and 2026")
print(calendar.leapdays(2000, 2026))

# ---------------------------------------
# 6. Month Range
# ---------------------------------------

print("\n6. Month Range")
first_day, total_days = calendar.monthrange(2026, 7)
print("First Weekday:", calendar.day_name[first_day])
print("Total Days:", total_days)

# ---------------------------------------
# 7. Month Calendar Matrix
# ---------------------------------------

print("\n7. Month Calendar Matrix")
print(calendar.monthcalendar(2026, 7))

# ---------------------------------------
# 8. Month Names
# ---------------------------------------

print("\n8. Month Names")
for month in calendar.month_name[1:]:
    print(month)

# ---------------------------------------
# 9. Weekday Names
# ---------------------------------------

print("\n9. Weekday Names")
for day in calendar.day_name:
    print(day)
