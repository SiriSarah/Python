# Example of While loop

number = int(input("Enter a number less than 10: "))

while number <= 10:
    # The same variable can be reused, numerical operators can be simplified.
    number *= 2 # It is same as number = number * 2

print(f"The number you have entered become, {number}")

# To do: Use an if condition, to check whether the entered number is actually less than 10.