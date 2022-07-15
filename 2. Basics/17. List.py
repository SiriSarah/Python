# List updates

num_of_sub = int(input("Enter the number of subjects you have: "))
mark_list = list()

for i in range(num_of_sub):
    marks = int(input(f"Enter the mark {i+1}: "))
    mark_list.append(marks)

print(mark_list)