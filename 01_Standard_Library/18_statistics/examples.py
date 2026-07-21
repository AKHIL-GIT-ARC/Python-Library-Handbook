"""
examples.py
Module: statistics

"""
from statistics import (
    mean,
    fmean,
    median,
    median_low,
    median_high,
    median_grouped,
    mode,
    multimode,
    variance,
    pvariance,
    stdev,
    pstdev,
    quantiles,
    geometric_mean,
    harmonic_mean
)


marks = [72, 85, 90, 78, 85, 92, 88, 76]
print("=" * 10)
print("1. mean()")
print("=" * 10)
print("Marks :", marks)
print("Mean  :", mean(marks))

print("\n" + "=" * 10)
print("2. fmean()")
print("=" * 10)
print("Fast Mean :", fmean(marks))

print("\n" + "=" * 10)
print("3. median()")
print("=" * 10)
print("Median :", median(marks))

print("\n" + "=" * 10)
print("4. median_low()")
print("=" * 10)
print("Lower Median :", median_low(marks))

print("\n" + "=" * 10)
print("5. median_high()")
print("=" * 10)
print("Higher Median :", median_high(marks))

print("\n" + "=" * 10)
print("6. median_grouped()")
print("=" * 10)
grouped_data = [10, 20, 20, 20, 30, 30, 40]
print("Grouped Median :", median_grouped(grouped_data))

print("\n" + "=" * 10)
print("7. mode()")
print("=" * 10)
print("Mode :", mode(marks))

print("\n" + "=" * 10)
print("8. multimode()")
print("=" * 10)
numbers = [1, 2, 2, 3, 3, 4]
print("Numbers :", numbers)
print("Multimode :", multimode(numbers))

print("\n" + "=" * 10)
print("9. variance()")
print("=" * 10)
print("Sample Variance :", variance(marks))

print("\n" + "=" * 10)
print("10. pvariance()")
print("=" * 10)
print("Population Variance :", pvariance(marks))

print("\n" + "=" * 10)
print("11. stdev()")
print("=" * 10)
print("Sample Standard Deviation :", stdev(marks))

print("\n" + "=" * 10)
print("12. pstdev()")
print("=" * 10)
print("Population Standard Deviation :", pstdev(marks))

print("\n" + "=" * 10)
print("13. quantiles()")
print("=" * 10)
scores = [45, 55, 10, 65, 70, 75, 80, 85, 90, 95]
print("Scores :", scores)
print("Quartiles :", quantiles(scores, n=4))

print("\n" + "=" * 10)
print("14. geometric_mean()")
print("=" * 10)
growth = [2, 8]
print("Numbers :", growth)
print("Geometric Mean :", geometric_mean(growth))

print("\n" + "=" * 10)
print("15. harmonic_mean()")
print("=" * 10)
speed = [10, 40]
print("Numbers :", speed)
print("Harmonic Mean :", harmonic_mean(speed))
