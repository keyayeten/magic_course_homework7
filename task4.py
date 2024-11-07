# Создайте класс Triangle, который имеет:

# Атрибуты a, b и c для хранения длины сторон.

# Метод is_valid, который проверяет, можно ли из этих
# сторон составить треугольник (сумма любых двух сторон
# должна быть больше третьей).

# Метод perimeter, который возвращает периметр треугольника,
# если он существует, или выводит сообщение "Треугольник недопустим".
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self):
        return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)

    def perimeter(self):
        if self.is_valid():
            p = self.a + self.b + self.c
            return print(f"Периметр треугольника: {p}")
        else:
            return print("Треугольник недопустим")


triangle = Triangle(2, 2, 8)
triangle.is_valid()
triangle.perimeter()
