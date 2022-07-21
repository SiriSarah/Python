class BankAccount:
  def __init__(self, customer, balance):
    self._customer = customer
    self._balance = balance

  def get_customer(self):
    return self._customer

  def get_balance(self):
    return self._balance

  def charge(self, price):
    if price > self._balance:  
      return False                           
    else:
      self._balance -= price
      return True
  
  def deposit(self, amount):
    if amount > 0:
        self._balance += amount
