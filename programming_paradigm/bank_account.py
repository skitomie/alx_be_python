class BankAccount:
    def __init__(self, amount, account_balance=0):
        self.account_balance = account_balance
        self.amount = amount

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
                           
    def withdraw(self, amount):
        if self.account_balance > amount:
                self.account_balance -= amount
        else: 
            return False
    
    def display_balance(self):
       balance = print(f"Current Balance: ${self.account_balance}")
       return balance