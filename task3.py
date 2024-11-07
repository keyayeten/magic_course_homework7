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
        cp_grade = sum(self.grades) / len(self.grades)
        return cp_grade
    

student = Student("Alex", 19, [5, 4, 5, 4, 4, 4, 3, 3])
student.add_grade(5)
print(student.average_grade())