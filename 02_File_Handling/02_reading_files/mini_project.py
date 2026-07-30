# Mini Project - Text File Analyzer

FILE_NAME = "sample.txt"

def analyze_file():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()
        # Count lines
        line_count = len(lines)
        # Count words
        word_count = 0
        for line in lines:
            word_count += len(line.split())
        # Count characters
        character_count = sum(len(line) for line in lines)
        print("FILE ANALYSIS")
        print("-" * 25)
        print("Lines:", line_count)
        print("Words:", word_count)
        print("Characters:", character_count)
        print("\nFile Content:")
        for number, line in enumerate(lines, start=1):
            print(f"{number}. {line.strip()}")
    except FileNotFoundError:
        print(f"{FILE_NAME} not found.")
analyze_file()