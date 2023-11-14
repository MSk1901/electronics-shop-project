import pytest

from src.item import Item


@pytest.fixture
def test_item():
    return Item("iPhone", 80000, 3)


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
