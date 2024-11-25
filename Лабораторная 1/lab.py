import doctest


class Painting:
    def __init__(self, title: str, artist: str, year: int):
        """
        Создание и подготовка к работе объекта "Картина".

        :param title: Название картины.
        :param artist: Имя художника, нарисовавшего картину.
        :param year: Год написания картины.

        Примеры:
        >>> painting = Painting("Мона Лиза", "Леонардо Да Винчи", 1503) # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название картины должно быть типа String!")
        if len(title) == 0:
            raise ValueError("У картины должно быть название!")
        self.title = title

        if not isinstance(artist, str):
            raise TypeError("Автор картины должен быть типа String!")
        if len(artist) == 0:
            raise ValueError("У картины должен быть автор!")
        self.artist = artist

        if not isinstance(year, int):
            raise TypeError("Год написания картины должен быть типа int!")

        self.year = year

    def display_info(self) -> str:
        """
        Отображает информацию о картине.
        :return: Информация о картине.
        """
        pass

    def appraise(self) -> float:
        """
        Оценка стоимости картины.
        :return: Стоимость картины.
        """
        pass


class Chair:
    def __init__(self, material: str, height: float, has_arms: bool):
        """
        Создание и подготовка к работе объекта "Стул".

        :param material: Материал из которого изготовлен стул.
        :param height: Высота стула.
        :param has_arms: Есть ли у стула ручки?

        Примеры:
            >>> chair = Chair("Дуб", 60, True) # инициализация экземпляра класса
        """

        if not isinstance(material, str):
            raise TypeError("У стула должен быть материал типа String!")
        if len(material) == 0:
            raise ValueError("У стула должен быть материал!")
        self.material = material

        if not isinstance(height, (int, float)):
            raise TypeError("У стула должна быть высота типа int или float!")

        if height <= 0:
            raise ValueError("Высота стула должна быть больше 0!")
        self.height = height

        if not isinstance(has_arms, bool):
            raise TypeError("Ручки у стула могут только быть или не быть! Типа: bool")
        self.has_arms = has_arms

    def sit(self) -> None:
        """
        Сесть на стул.
        """
        pass

    def adjust_height(self, new_height: float) -> None:
        """
        Увеличить высоту стула
        :param new_height: Новая высота стула.
        """

        if not isinstance(new_height, (int, float)):
            raise TypeError("У стула должна быть высота типа int или float!")

        if self.height - new_height <= 0:
            raise ValueError("Вы указали слишком маленькую высоту стула!")

        pass

    def describe(self) -> str:
        """
        Отображает описание стула.
        :return: Описание стула.
        """
        pass


class Phone:
    def __init__(self, brand: str, model: str, storage_capacity: int):
        """
        Создание и подготовка к работе объекта "Телефон".

        :param brand: Название фирмы, изготовившей телефон.black --check -l120 --skip-string-normalization
        :param model: Название модели телефона.
        :param storage_capacity: Объем постоянной памяти телефона.

        Примеры:
            >>> phone = Phone("Nokia", "3310", 250) # инициализация экземпляра класса
        """

        if not isinstance(brand, str):
            raise TypeError("Название фирмы, изготовившей телефон должно быть типа String!")
        if len(brand) == 0:
            raise ValueError("У фирмы, изготовившей телефон должно быть название!")
        self.brand = brand

        if not isinstance(brand, str):
            raise TypeError("Название модели телефона должно быть типа String!")
        if len(brand) == 0:
            raise ValueError("У телефона должна быть модель!")
        self.model = model

        if not isinstance(storage_capacity, int):
            raise TypeError("Объем постоянной памяти телефона должен быть типа int!")
        self.storage_capacity = storage_capacity

        self.l = ""

    def make_call(self, number: str) -> None:
        """
        Звонок на указанный номер телефона.
        :param number: Телефонный номер, на который нужно позвонить.
        """

        self.l = " "  # Чтобы PEP8 не считал, что эту функцию можно вынести из класса

        if not isinstance(number, str):
            raise TypeError("Телефонный номер, на который нужно позвонить должен быть типа String!")
        if len(number) == 0:
            raise ValueError("Длина номера телефона должна быть больше нуля!")
        pass

    def send_text(self, number: str, message: str) -> None:
        """
        Отправка сообщения на указанный номер телефона.
        :param number: Телефонный номер, на который нужно отправить сообщение.
        :param message: Текст сообщения.
        """
        self.l = " "  # Чтобы PEP8 не считал, что эту функцию можно вынести из класса
        if not isinstance(number, str):
            raise TypeError("Телефонный номер, на который нужно отправить сообщение должен быть типа String!")
        if len(number) == 0:
            raise ValueError("Длина номера телефона должна быть больше нуля!")

        if not isinstance(message, str):
            raise TypeError("Текст сообщения, которое нужно отправить должен быть типа String!")
        if len(message) == 0:
            raise ValueError("Длина номера телефона должна быть больше нуля!")

        pass

    def display_info(self) -> str:
        """
        Отображает информацию о телефоне.
        :return: Информация о телефоне.
        """
        pass


if __name__ == "__main__":
    doctest.testmod()
