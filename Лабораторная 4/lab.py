import doctest


class Animal:
    """
    Базовый класс для всех животных.
    Создание и подготовка к работе объекта "Животное"

    Свойства:
    name (str): Имя животного.
    name приватное, так как переименовывать животное аморально :))

    Атрибуты:
    age (int): Возраст животного.

    Примеры:
    >>> animal = Animal(name="Животное", age=5)
    >>> print(animal)
    Животное, 5 лет
    >>> repr(animal)
    'Animal(name=Животное, age=5)'
    >>> animal.speak()
    Traceback (most recent call last):
        ...
    NotImplementedError: Этот метод должен быть переопределен в дочернем классе
    """

    def __init__(self, name: str, age: int):
        self._name = name
        self.age = age

    @property
    def name(self):
        return self._name

    def __str__(self) -> str:
        return f"{self.name}, {self.age} лет"

    def __repr__(self) -> str:
        return f"Animal(name={self.name}, age={self.age})"

    def speak(self) -> str:
        raise NotImplementedError("Этот метод должен быть переопределен в дочернем классе")


class Dog(Animal):
    """
    Создание и подготовка к работе объекта "Собака"

    Атрибуты:
    breed (str): Порода собаки.

    Примеры:
    >>> dog = Dog(name="Бобик", age=3, breed="Лабрадор")
    >>> print(dog)
    Бобик, 3 лет, порода: Лабрадор
    >>> repr(dog)
    'Dog(name=Бобик, age=3, breed=Лабрадор)'
    >>> dog.speak()
    'Гав-гав'
    """

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def __str__(self) -> str:
        return f"{self.name}, {self.age} лет, порода: {self.breed}"

    def __repr__(self) -> str:
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

    def speak(self) -> str:
        return "Гав-гав"


class Cat(Animal):
    """
    Создание и подготовка к работе объекта "Кошка"

    Атрибуты:
    color (str): Цвет кошки.

    Примеры:
    >>> cat = Cat(name="Мурка", age=2, color="Черный")
    >>> print(cat)
    Мурка, 2 лет, цвет: Черный
    >>> repr(cat)
    'Cat(name=Мурка, age=2, color=Черный)'
    >>> cat.speak()
    'Мяу'
    """

    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color

    def __str__(self) -> str:
        return f"{self.name}, {self.age} лет, цвет: {self.color}"

    def __repr__(self) -> str:
        return f"Cat(name={self.name}, age={self.age}, color={self.color})"

    def speak(self) -> str:
        return "Мяу"


if __name__ == "__main__":
    doctest.testmod()

    dog1 = Dog(name="Бобик", age=3, breed="Лабрадор")
    cat1 = Cat(name="Мурка", age=2, color="Черный")

    print(dog1)  # Бобик, 3 лет, порода: Лабрадор
    print(cat1)  # Мурка, 2 лет, цвет: Черный

    print(dog1.speak())  # Гав-гав
    print(cat1.speak())  # Мяу
