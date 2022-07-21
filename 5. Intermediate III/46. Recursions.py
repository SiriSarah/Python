# Example of recursive function
def recursion_fibonacci(n):
    if n <= 1:
        return n
    else:
        # The function is calling itself, with different parameters
        return(recursion_fibonacci(n-1) + recursion_fibonacci(n-2))

# Getting the first 25 fibonacci numbers
for i in range(1, 26):
    print(recursion_fibonacci(i))