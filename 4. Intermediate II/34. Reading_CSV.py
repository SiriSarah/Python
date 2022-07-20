# Import the CSV library
import csv, os # Multiple libraries can be imported with , sign in a single line.

def write_file(filename):
    file_handler = open(filename, "w", encoding="UTF-8")
    writer = csv.writer(file_handler)
    header = ["Index", "Multiplied by 2", "Multiplied by 3"]
    writer.writerow(header)

    for i in range(1, 11):
        row = [i, i*2, i*3] # Why are we creating a variable here?
        writer.writerow(row)

    file_handler.close() # What happens if we didn't close?


def read_file(filename):
    file_handler = open(filename)
    reader = csv.reader(file_handler)

    for row in reader:
        print(",".join(row))    # What is this??? 

    file_handler.close()


filename = os.path.dirname(__file__) + "/output.csv"

if os.path.exists(filename):
    read_file(filename)
else:
    write_file(filename)

# To do: Simplify the existing steps to achieve the same results. Read the comments inside the code and try to figure out the answers.