from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim: int):
        """
        Создание экземпляра класса Phone.

        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        if number_of_sim <= 0 or not isinstance(number_of_sim, int):
            raise ValueError(
                "Количество физических SIM-карт должно быть "
                "целым числом больше нуля.")
        else:
            self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number):
        if new_number <= 0 or not isinstance(new_number, int):
            raise ValueError(
                "Количество физических SIM-карт должно "
                "быть целым числом больше нуля.")
        else:
            self.__number_of_sim = new_number

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}', "
                f"{self.price}, {self.quantity}, {self.__number_of_sim})")

    def __add__(self, other):
        """
        Сложение количества экземпляров класса Phone и Item
        (сложение по количеству товара в магазине)
        """
        if isinstance(other, (Item, Phone)):
            return self.quantity + other.quantity
        raise ValueError("Сложение возможно только с экземпляром класса Item")
