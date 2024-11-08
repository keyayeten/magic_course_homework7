# Создайте класс Student, который имеет:

# Атрибуты name, age и grades (список оценок).

# Метод add_grade(grade), который добавляет новую оценку
# в список.

# Метод average_grade, который возвращает средний балл студента.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self,grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades)/len(self.grades) if len(self.grades) != 0 else None