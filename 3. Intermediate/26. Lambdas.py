# Python uses, special functions called as lambdas

def function_add(a, b):
    return a + b

print(function_add(4, 5))

# The above function can be rewritten in lambda or single line function.
function_add_lambda = lambda a, b : a + b

print(function_add_lambda(4, 5))

# To do: create the lambda inside function and see what happens.
# Create multiplication tables with the lambdas.