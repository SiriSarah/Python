names_list = ["Alphabet", "Meta", "SiriSarah LLC", "Google", "Facebook", "WhatsApp"]

names_list.sort()
print(names_list)

names_list.reverse()
print(names_list)

def find_max(given_list):
    max = given_list[0]
    for i in range(1, len(given_list)):
        if given_list[i] > given_list[i-1]:
            max = given_list[i]
        else:
            max = given_list[i]
    
    return max

number_list =  [5, 3, 1, 0, 10, 12]
print(find_max(number_list))

# Alternatively, we can do this.
number_list.sort()
print(f"The largest number in the list is: {number_list[-1]}")
print(f"The smallest number in this list is: {number_list[0]}")

# Compare the functions, and find which one uses less memory, and time.
# The calculation of memory is called as "Space Complexity"
# Calculating the time, is called as "Time Complexity"
# Increased loops, increase both time and space complexity
# We have to calculate, both of them before running plenty of loops in our program.