class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
     
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False
                           
    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:    
            amount =- self.account_balance
            return True
        else:
            return False    
           
    def display_balance(self):
       balance = print(f"Current Balance: ${self.account_balance:.2f}")
       return balance