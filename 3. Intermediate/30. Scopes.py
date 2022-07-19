item_value  = 0  # Example of Global Scope, usually represented in CAPS

def function_to_update(item_value):
    print(item_value)

    # Yes, function can have nested functions 
    def function_to_increase():     
        item_value = 2
        print(item_value)

    def function_to_decrease():
        global item_value
        print(item_value)
        item_value = 1
        print(item_value)

    function_to_increase()
    function_to_decrease()

function_to_update(item_value)

# To do: Play with functions with return values, and then try to assign the values before calling global.