import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone


@pytest.fixture
def test_item():
    return Item("iPhone", 80000, 3)


@pytest.fixture
def test_phone():
    return Phone("iPhone", 80000, 5, 1)


def test_item_init(test_item):
    name, price, num = test_item.name, test_item.price, test_item.quantity
    assert f"{name} {price} {num}" == "iPhone 80000 3"


def test_item_repr(test_item):
    assert repr(test_item) == "Item('iPhone', 80000, 3)"


def test_item_str(test_item):
    assert str(test_item) == 'iPhone'


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 240000


def test_apply_discount(test_item):
    Item.pay_rate = 0.8
    test_item.apply_discount()
    assert test_item.price == 64000


def test_name_getter(test_item):
    assert test_item.name == "iPhone"


def test_name_setter(test_item):
    test_item.name = "Samsung"
    assert test_item.name == "Samsung"


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_instantiate_from_csv_no_file():
    with pytest.raises(FileNotFoundError):
        assert Item.instantiate_from_csv(
            "item.csv") == "Отсутствует файл item.csv"


def test_instantiate_from_csv_damaged_file():
    with pytest.raises(InstantiateCSVError):
        assert Item.instantiate_from_csv(
            "../src/items_damaged.csv") == "Файл item.csv поврежден"


@pytest.mark.parametrize("data, expected_result", [("5", 5),
                                                   ("5.0", 5),
                                                   ("5.5", 5),
                                                   ("abc", None)
                                                   ])
def test_string_to_number(data, expected_result):
    assert Item.string_to_number(data) == expected_result


def test_add(test_item, test_phone):
    assert test_item + test_phone == 8
