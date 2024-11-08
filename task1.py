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
        return f'Название: {self.title}, Автор: {self.author}, Год издания: {self.year}'

info_book = Book("Мастер и Маргаритта", "Булгаков", 1920)
info_book2 = Book("Идиот", "Достоевкий", 1920)
info_book3 = Book("Парус", "Пушкин", 1920)
print(info_book.get_info())
print(info_book2.get_info())
print(info_book3.get_info())
