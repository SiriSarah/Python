print(1+2)
print("SiriSarah"+"LLC")

# The same operator(+) is used in the above two statements but behaves differently.
# Comment the first two line after understanding it

class complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # Overloading the "+" operator
    def __add__(self, other):
        return self.real + other.real, self.imaginary + other.imaginary
    
    def print(self):
        print(str(self.real) + "+" + str(self.imaginary) + "j") 
        # In python, complex part is represented with j

c1 = complex(2, 3)
c1.print()
c2 = complex(4, 5)
c2.print()
c3 = c1 + c2
print(c3)

# To do: Update the logic to print c3 using, c3.print() command!
# Create operator overloading for other numerical and comparison operators. 