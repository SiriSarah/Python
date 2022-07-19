import os

filename = os.path.dirname(__file__) + "/24. Read_Write.py.txt"
if os.path.exists(filename):
    os.remove(filename)
    print("File deletion successful!")
else:
    print("The file is already deleted!")

# To do: Try to remove the directory use, rmdir command. 