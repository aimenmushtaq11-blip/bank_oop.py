class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def show(self):
        return f"{self.owner}: {self.balance:.2f}"


if __name__ == "__main__":
    acct = Account("Aisha", 100.0)
    acct.deposit(50.0)
    acct.withdraw(30.0)
    print(acct.show())   # Aisha: 120.00


