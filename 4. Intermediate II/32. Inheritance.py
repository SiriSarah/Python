# Inheritance is creating new class with existing class properties

class Company:
    def __init__(self, name):
            self.name = name

    def pretty_print(self):
        print(f"The name of the company is: {self.name} ")

class LLC(Company):
    def add_owner(self, owner_name):
        self.owner_name = owner_name

    def pretty_print(self):
        print(f"The owner of the LLC is: {self.owner_name}")
        return super().pretty_print() 

class Corporate(Company):
    share_holders = []
    def add_shareholders(self, share_holder):
        self.share_holders.append(share_holder) 
    
    def list_of_shareholders(self):
        for share_holder in self.share_holders:
            print(share_holder)

    def pretty_print(self):
        print(f"The Share holders of the Corporation are: {self.list_of_shareholders()}")
        return super().pretty_print() 

llc = LLC("SiriSarah LLC")
llc.add_owner("Mythili Mohan")

corp = Corporate("Google")
corp.add_shareholders("Mythili Mohan")
corp.add_shareholders("Mark Z")
corp.add_shareholders("Sundar P")

c = Company("Mannar & Co.,")

c.pretty_print()
llc.pretty_print()
corp.pretty_print()

# To do: Play with every class, and try to understand the flow, Rearrange the steps to print the output to make sense.