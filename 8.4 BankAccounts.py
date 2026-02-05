class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    print(f'Deposited ${amount}. New balance is ${self.balance}.')

  def withdraw(self, amount):
    self.balance -= amount
    print(f"Withdrew ${amount}. New balance is ${self.balance}.")

  def display_balance(self):
    self.balance = self.balance
    print(f"Current balance is ${self.balance}.")

account1 = BankAccount("John", "Doe", "123456", "Checking", "7890", 1000)

account1.deposit(96)
account1.withdraw(25)
account1.display_balance()

print(vars(account1))
