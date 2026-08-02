# Mini Project - Activity Logger

FILE_NAME = "activity.log"

# Write activities to log file
file = open(FILE_NAME, "w", encoding="utf-8")
while True:
    activity = input("Enter activity (type 'exit' to stop): ")
    if activity.lower() == "exit":
        break
    file.write(activity + "\n")
    # Save data immediately
    file.flush()
print("\nBefore closing:", file.closed)
file.close()
print("After closing:", file.closed)
print("\nActivities saved successfully.")