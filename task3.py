# Создайте класс Student, который имеет:

# Атрибуты name, age и grades (список оценок).

# Метод add_grade(grade), который добавляет новую оценку
# в список.

# Метод average_grade, который возвращает средний балл студента.

class Student():
    def __init__(self, name, age, grades: list):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        suma = 0
        for i in self.grades:
            suma += i
        b = suma / len(self.grades)
        return float(round(b, 2))

avg = Student("Oleg", 20, [2, 5, 5])
avg2 = Student("Asya", 27, [4, 5, 5])
avg3 = Student("Maria", 18, [3, 3, 3])
avg.add_grade(2)
print(avg.average_grade())
avg.add_grade(5)
print(avg2.average_grade())
avg.add_grade(4)
print(avg3.average_grade())

