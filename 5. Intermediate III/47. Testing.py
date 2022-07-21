# Importing the module from different local file

# Try and understand the below import options.
# from .BankAccount import BankAccount
# import BankAccount

from BankAccount import *

def Unit_Test():
    customer = []
    customer.append(BankAccount('SiriSarah LLC', 2500))
    customer.append(BankAccount('Siri', 5000))
    customer.append(BankAccount('Sarah', 8000))
    
    for value in range(1, 10):
        customer[0].charge(value)
        customer[1].charge(2*value)
        customer[2].charge(3*value)

    for c in range(3):
        print('Customer =', customer[c].get_customer())
        print('Balance =', customer[c].get_balance())
        while customer[c].get_balance() < 3500:
            customer[c].deposit(500)
            print('New balance =', customer[c].get_balance())
        print()

if __name__ == '__main__':
    # Do not run the unit tests, if it is used by another module
    Unit_Test()