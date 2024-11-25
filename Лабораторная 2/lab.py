class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books: list[Book] = None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

    def __str__(self) -> str:
        return f"Library with {len(self.books)} books"

    def __repr__(self) -> str:
        return f"Library(books={self.books})"


if __name__ == "__main__":
    # Создание библиотеки
    library = Library()

    # Добавление книг
    book1 = Book(id_=library.get_next_book_id(), name="Python Programming", pages=350)
    book2 = Book(id_=library.get_next_book_id(), name="Data Science with Python", pages=400)

    # Добавляем книги в библиотеку
    library.books.append(book1)
    library.books.append(book2)

    print(library)  # Library with 2 books

    # Получение индекса книги по ID
    book_index = library.get_index_by_book_id(1)
    print(book_index)  # 0

    # Примеры __str__ и __repr__
    print(str(book1))  # Книга "Python Programming"
    print(repr(book1))  # Book(id_=1, name='Python Programming', pages=350)
