# Mini Project - Student Result Checker

def check_marks():
    try:
        marks = int(input("Enter marks (0-100): "))
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")
    except ValueError as error:
        print("Error:", error)
    else:
        if marks >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")
    finally:
        print("Result checking completed.")
check_marks()