fruit_bucket = {
    "apple",
    "banana",
    "cantaloupe"
}

# print(fruit_bucket[0])

""" for fruit in fruit_bucket:
    print(fruit) """

fruit_iteration = iter(fruit_bucket)
print(fruit_iteration)
print(next(fruit_iteration))
print(next(fruit_iteration))
print(next(fruit_iteration))
print(next(fruit_iteration)) # This will throw error, since iteration ends

# To do: Try the iteration with list, set, and tuple.