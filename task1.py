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
        return print(f"{self.title} {self.author} {self.year}")

book = Book("Гарри Поттер", "Роллинг", 1997)
book1 = Book("Властелин Колец", "Толкин", 1954)
book.get_info()
book1.get_info()
