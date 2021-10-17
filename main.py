import os
import send2trash

user_extension = input("What file extensions are you looking to delete? (i.e .txt) => ")
root = input("Please enter the directory to search => ")

try:
    os.chdir(root)
except FileNotFoundError:
    print("This file does not exist or you have passed in the incorrect format")
    print('\n Make sure you are using double backslash')
else:
    files_deleted = []
    for root, dirname, file, in os.walk(os.getcwd()):
        print(f"Searching root: {root}")
        for f in file:
            name, extension = os.path.splitext(f)
            if extension == user_extension:
                path = os.path.join(root, f)
                files_deleted.append(name)
                send2trash.send2trash(path)
    if len(files_deleted) == 0:
        print(f"\nno files with '{user_extension}' found")
    else:
        for x in files_deleted:
            if len(files_deleted) == 0:
                print(f"no files with {user_extension}' extension found")
            else:
                print(f"\ndeleted '{x}'")
