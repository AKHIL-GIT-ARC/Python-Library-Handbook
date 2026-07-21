"""
mini_project.py
Module: statistics

Student Statistics Analyzer
Demonstrates the practical use of the statistics module.
"""
from statistics import (
    mean,
    median,
    mode,
    variance,
    stdev,
    quantiles
)

marks = [72, 85, 90, 78, 85, 92, 88, 76]

def show_marks():
    print("\nStudent Marks")
    print(marks)

def calculate_mean():
    print("\nAverage Marks:", mean(marks))

def calculate_median():
    print("\nMedian Marks:", median(marks))

def calculate_mode():
    print("\nMode:", mode(marks))

def calculate_variance():
    print("\nVariance:", variance(marks))

def calculate_standard_deviation():
    print("\nStandard Deviation:", stdev(marks))

def calculate_quartiles():
    print("\nQuartiles:")
    print(quantiles(marks, n=4))

def performance_summary():
    print("\nPerformance Summary")
    print("-" * 20)
    print("Highest Marks :", max(marks))
    print("Lowest Marks  :", min(marks))
    print("Average Marks :", round(mean(marks), 2))
    print("Median        :", median(marks))
    print("Mode          :", mode(marks))
    print("Variance      :", round(variance(marks), 2))
    print("Std Deviation :", round(stdev(marks), 2))


while True:
    print("\n" + "=" * 30)
    print("   STUDENT STATISTICS ANALYZER")
    print("=" * 30)
    print("1. Show Student Marks")
    print("2. Calculate Mean")
    print("3. Find Median")
    print("4. Find Mode")
    print("5. Calculate Variance")
    print("6. Calculate Standard Deviation")
    print("7. Generate Quartiles")
    print("8. Performance Summary")
    print("9. Exit")

    choice = input("\nEnter Choice: ")
    if choice == "1":
        show_marks()
    elif choice == "2":
        calculate_mean()
    elif choice == "3":
        calculate_median()
    elif choice == "4":
        calculate_mode()
    elif choice == "5":
        calculate_variance()
    elif choice == "6":
        calculate_standard_deviation()
    elif choice == "7":
        calculate_quartiles()
    elif choice == "8":
        performance_summary()
    elif choice == "9":
        print("\nThank You For Using Student Statistics Analyzer!")
        break
    else:
        print("Invalid Choice!")