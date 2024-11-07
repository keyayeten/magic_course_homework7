# Создайте класс Book, который имеет:

# Атрибуты title, author и year.
# Метод get_info, который возвращает строку с информацией о книге в формате:
# "Название: [title], Автор: [author], Год издания: [year]".

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return (f'Название: {self.title}, Автор: {self.author}, Год издания: {self.year}')


book = Book("Гарри Поттер и философский камень", "Джоан Роулинг", 1997)
print(book.get_info())
