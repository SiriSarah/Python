from time import time
import timeit

# Statements can be passed and we can calculate the run time
time_required = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"It took {round(time_required, 4)} seconds")

# To do: Use the timeit function in singly and doubly linked list and compare the performance.
