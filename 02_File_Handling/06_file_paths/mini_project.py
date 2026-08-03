# Mini Project - File & Folder Checker

import os
path = input("Enter file/folder path: ")
if os.path.exists(path):
    print("\nPath exists.")
    if os.path.isfile(path):
        print("Type: File")
    elif os.path.isdir(path):
        print("Type: Folder")
    print("Absolute Path:", os.path.abspath(path))
else:
    print("\nPath does not exist.")