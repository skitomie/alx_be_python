class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
     
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
                           
    def withdraw(self, amount):
        if amount <= self.account_balance:
                self.account_balance -= amount
        else: 
            return False
    
    def display_balance(self):
       balance = print(f"Current Balance: ${self.account_balance:.2f}")
       return balance