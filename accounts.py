import datetime
import pytz


class Account:
    """ simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = []
        self._transaction_list.append((Account._current_time(), balance))
        print("account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("the amount must be greater than 0 and less that the total balance")
        self.show_balance()

    def show_balance(self):
        print("balance is {}".format(self._balance))
# in a static method its best to leave the class name instead of using self
    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposit"
            else:
                tran_type = "withdraw"
                amount *= -1
            print("{:6} {} on {} (local time was {}".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account("tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    tim.withdraw(500)

    tim.withdraw(6000)

    tim.show_transactions()

    bob = Account("bob", 800)
    bob.deposit(100)
    bob.withdraw(200)
    bob.show_transactions()
