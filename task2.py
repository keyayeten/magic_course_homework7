# Создайте класс BankAccount, который имеет:

# Атрибут balance, начальное значение которого равно 0.

# Метод deposit(amount), который увеличивает баланс на
# сумму amount.

# Метод withdraw(amount), который уменьшает баланс на сумму
# amount, если на счете достаточно средств;
# если недостаточно, выведите сообщение "Недостаточно средств".

# Метод get_balance, который возвращает текущий баланс.

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств")

    def get_balance(self):
        return self.balance


my_money = BankAccount()
my_money.deposit(1500)
my_money.withdraw(1000)
print(my_money.get_balance())
