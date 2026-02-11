# =>> Mini project using all OOPs concepts

from abc import ABC, abstractmethod


# ------------------ Abstraction ------------------
class Account(ABC):
    bank_name = "Pratvi Bank Pvt Ltd"   # Class variable

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance   # Encapsulation (private variable)

    # Getter method (Encapsulation)
    def get_balance(self):
        return self.__balance

    # Setter method (Encapsulation)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    @abstractmethod
    def account_type(self):
        pass

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def bank_rules():
        print("1. Minimum balance ₹1000 required.")
        print("2. KYC mandatory.")


# ------------------ Inheritance ------------------

class SavingsAccount(Account):

    def account_type(self):   # Polymorphism (Method Overriding)
        print("Account Type: Savings Account")


class CurrentAccount(Account):

    def account_type(self):   # Polymorphism (Method Overriding)
        print("Account Type: Current Account")


# ------------------ Main Program ------------------

acc1 = SavingsAccount(101, "Pratvi", 5000)
acc2 = CurrentAccount(102, "Devarsh", 10000)

print("Bank Name:", Account.bank_name)

acc1.account_type()
acc1.deposit(2000)
acc1.withdraw(1000)
print("Balance:", acc1.get_balance())

print("------------")

acc2.account_type()
acc2.withdraw(3000)
print("Balance:", acc2.get_balance())

print("------------")

Account.bank_rules()
    



