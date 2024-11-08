# Создайте класс BankAccount, который имеет:

# Атрибут balance, начальное значение которого равно 0.

# Метод deposit(amount), который увеличивает баланс на
# сумму amount.

# Метод withdraw(amount), который уменьшает баланс на сумму
# amount, если на счете достаточно средств;
# если недостаточно, выведите сообщение "Недостаточно средств".

# Метод get_balance, который возвращает текущий баланс.

class BankAccount:
    def __init(self):
        self.balance = 0

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance>= amount:
            self.balance -=amount
            return 1
        else:
            print("Недостаточно средств")
            return -1
