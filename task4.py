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
        lst = sorted([self.a,self.b, self.c])
        return lst[0]+lst[1] > lst[2]

    def perimeter(self):
        if self.is_valid():
            return self.a+self.b+self.c
        else:
            print("Треугольник недопустим")
            return None

tr = Triangle(1,2,3)
print(tr.perimeter())