# Создайте класс Triangle, который имеет:

# Атрибуты a, b и c для хранения длины сторон.

# Метод is_valid, который проверяет, можно ли из этих
# сторон составить треугольник (сумма любых двух сторон
# должна быть больше третьей).

# Метод perimeter, который возвращает периметр треугольника,
# если он существует, или выводит сообщение "Треугольник недопустим".
class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self):
        return self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b




    def perimeter(self):
        if self.is_valid():
            return self.a + self.b + self.c
        return 'Треугольник недопустим'


per = Triangle(5, 5, 5)
per.is_valid()
print(per.perimeter())


per2 = Triangle(10, 5, 3)
per2.is_valid()
print(per2.perimeter())


per3 = Triangle(3, 3, 7)
per3.is_valid()
print(per3.perimeter())

per4 = Triangle(4, 6, 5)
per4.is_valid()
print(per4.perimeter())

per5 = Triangle(12, 6, 4)
per5.is_valid()
print(per5.perimeter())