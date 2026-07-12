import glob
while True:
    print("\n" + "=" * 30)
    print("      FILE SEARCH UTILITY")
    print("=" * 30)
    print("1. Search Python Files")
    print("2. Search Text Files")
    print("3. Search Images")
    print("4. Search by Extension")
    print("5. Recursive Search")
    print("6. Search by Filename")
    print("7. Display Total Matches")
    print("8. Exit")

    choice = input("\nEnter Choice: ")
    if choice == "1":
        files = glob.glob("practice_files/**/*.py", recursive=True)
        print("\nPython Files")
        if files:
            for file in files:
                print(file)
        else:
            print("No Python files found.")

    elif choice == "2":
        files = glob.glob("practice_files/**/*.txt", recursive=True)
        print("\nText Files")
        if files:
            for file in files:
                print(file)
        else:
            print("No text files found.")

    elif choice == "3":
        files = glob.glob("practice_files/**/*.*", recursive=True)
        images = []
        for file in files:
            if file.endswith((".jpg", ".png", ".jpeg")):
                images.append(file)
        print("\nImage Files")
        if images:
            for image in images:
                print(image)
        else:
            print("No image files found.")

    elif choice == "4":
        extension = input("Enter Extension (py/txt/png/jpg): ").strip(".")
        pattern = f"practice_files/**/*.{extension}"
        files = glob.glob(pattern, recursive=True)
        print(f"\n.{extension} Files")
        if files:
            for file in files:
                print(file)
        else:
            print("No matching files found.")

    elif choice == "5":
        pattern = input("Enter Search Pattern (Example: *.py): ")
        files = glob.glob(
            f"practice_files/**/{pattern}",
            recursive=True
        )
        print("\nSearch Results")
        if files:
            for file in files:
                print(file)
        else:
            print("No matching files found.")

    elif choice == "6":
        filename = input("Enter File Name: ")
        files = glob.glob(
            f"practice_files/**/{filename}",
            recursive=True
        )
        print("\nSearch Results")
        if files:
            for file in files:
                print(file)
        else:
            print("File not found.")

    elif choice == "7":
        files = glob.glob("practice_files/**/*", recursive=True)
        total = len([file for file in files if "." in file])
        print("\nTotal Files:", total)

    elif choice == "8":
        print("\nThank you for using File Search Utility!")
        break

    else:
        print("Invalid Choice! Please try again.")