__author__ = 'Akerson'


class BankAccount(object):

    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.fees = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.fees += 5
            self.balance -= 5

    def get_balance(self):
        return self.balance

    def get_fees(self):
        return self.fees


