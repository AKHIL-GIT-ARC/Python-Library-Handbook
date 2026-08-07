# Mini Project - Student Report

name = input("Enter student name: ")
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))
print("\n" + "=" * 35)
print(f"{'STUDENT REPORT ':^35}")
print("=" * 35)

print(f"{'Name':<15}: {name}")
print(f"{'Marks':<15}: {marks:.2f}")
print(f"{'Attendance':<15}: {attendance:.1f}%")

print("-" * 35)
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"
print(f"{'Grade':<15}: {grade}")
print("=" * 35)