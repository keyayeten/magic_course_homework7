# Создайте класс Student, который имеет:

# Атрибуты name, age и grades (список оценок).

# Метод add_grade(grade), который добавляет новую оценку
# в список.

# Метод average_grade, который возвращает средний балл студента.
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        count = 0
        for i in self.grades:
            count += i
        return print(count / len(self.grades))


student = Student("Alex", 18, [5, 2, 5])
student.add_grade(3)
student.average_grade()
