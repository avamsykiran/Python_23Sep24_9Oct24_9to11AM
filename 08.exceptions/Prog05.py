
class NegativeValueAmountException(Exception):
    pass

class InsufficientBalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,openingBalance):
        self.balance=openingBalance

    def deposite(self,amount):
        if amount<0:
            raise NegativeValueAmountException
        self.balance+=amount
    
    def withdraw(self,amount):
        if amount<0:
            raise NegativeValueAmountException
        if self.balance<amount :
            raise InsufficientBalanceException
        self.balance-=amount

acc = BankAccount(10000)
print("Bal: {}",acc.balance)

shallContinue = True

while shallContinue:
    choice = input("Choose (d/w/q): ")

    try:
        if choice=="d" or choice=="D":
            amt = int(input("Enter amount: "))
            acc.deposite(amt)
            print("Bal: {}",acc.balance)
        elif choice=="w" or choice=="W":
            amt = int(input("Enter amount: "))
            acc.withdraw(amt)
            print("Bal: {}",acc.balance)
        elif choice=="q" or choice=="Q":
            print("App closed")
            shallContinue=False
        else:
            print("Unknown choice")
    except InsufficientBalanceException as e:
        print("Can not withdraw as the balance is not sufficient")
    except NegativeValueAmountException:
        print("amount entered cannot be in negative for Bank transactions")

