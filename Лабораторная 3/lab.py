class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть типа int!")
        if value < 1:
            raise ValueError("Количество страниц должно быть больше 0!")

        self._pages = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise TypeError("Продолжительность аудиокниги должна быть типа float!")
        if value < 1:
            raise ValueError("Продолжительность аудиокниги должна быть больше 0!")

        self._duration = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    # Создание экземпляра класса Book
    book = Book(name="Мастер и Маргарита", author="Михаил Булгаков")
    print(book)  # Книга Мастер и Маргарита. Автор: Михаил Булгаков
    print(repr(book))  # Book(name='Мастер и Маргарита', author='Михаил Булгаков')

    # Создание экземпляра класса PaperBook
    paper_book = PaperBook(name="Мастер и Маргарита", author="Михаил Булгаков", pages=480)
    print(paper_book)  # Книга Мастер и Маргарита. Автор: Михаил Булгаков
    print(repr(paper_book))  # PaperBook(name='Мастер и Маргарита', author='Михаил Булгаков', pages=480)

    # Создание экземпляра класса AudioBook
    audio_book = AudioBook(name="Мастер и Маргарита", author="Михаил Булгаков", duration=500)
    print(audio_book)  # Книга Мастер и Маргарита. Автор: Михаил Булгаков
    print(repr(audio_book))  # AudioBook(name='Мастер и Маргарита', author='Михаил Булгаков', duration=500)
