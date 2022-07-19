# Handling Errors are important in any programming language

try:
    a_number = int(input("Enter an integer number: "))

except ValueError:
    print("You have entered an non integer!")

# To do: Check for different type of common errors can occur like TypeError, ValueError, IndexError and etc.,