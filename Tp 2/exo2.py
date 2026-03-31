class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def deposif(self, amount):
        if amount > 0 :
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else :
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance ")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")
    
    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"BankAccount(owner={self.__owner}, balance={self.__balance}, account={self.account_number})"
    



acc1 = BankAccount("Manel", 500)
print(acc1.__balance)
#private attributes are name-mangled internally
