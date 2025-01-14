import csv
import os
from math import floor


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    PATH_CSV = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "src", "items.csv")

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.__name}', "
                f"{self.price}, {self.quantity})")

    def __str__(self):
        return self.__name

    def __add__(self, other):
        """
        Сложение количества экземпляров классов
        (сложение по количеству товара в магазине)
        """
        if issubclass(other.__class__, Item):
            return self.quantity + other.quantity
        raise ValueError(
            "Сложение возможно только с экземпляром подкласса Item")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Возвращает наименование товара
        """
        return self.__name

    @name.setter
    def name(self, new_name) -> None:
        """
        Изменяет наименование товара
        """
        if len(new_name) < 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, filename: str | None = PATH_CSV) -> None:
        """
        Инициализирует экземпляры класса данными из файла csv
        """
        cls.all.clear()
        try:
            with open(filename, newline="",
                      encoding="windows-1251'", errors="replace") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row["name"]
                    price = int(row["price"])
                    quantity = int(row["quantity"])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        except Exception:
            raise InstantiateCSVError

    @staticmethod
    def string_to_number(data: str) -> int | None:
        """
        Возвращает число из числа-строки
        """
        if data.isdigit():
            return int(data)
        elif "." in data:
            return floor(float(data))
        else:
            return None


class InstantiateCSVError(Exception):

    def __init__(self):
        self.message = "Файл item.csv поврежден"

    def __str__(self):
        return self.message
