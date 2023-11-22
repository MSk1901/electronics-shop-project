import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def test_item():
    return Item("iPhone", 80000, 3)


@pytest.fixture
def test_phone():
    return Phone("iPhone", 80000, 5, 1)


def test_item_init(test_phone):
    name, price, num, sim = (test_phone.name,
                             test_phone.price,
                             test_phone.quantity,
                             test_phone.number_of_sim)
    assert f"{name} {price} {num} {sim}" == "iPhone 80000 5 1"


def test_item_repr(test_phone):
    assert repr(test_phone) == "Phone('iPhone', 80000, 5, 1)"


def test_item_str(test_phone):
    assert str(test_phone) == 'iPhone'


def test_add(test_phone, test_item):
    assert test_phone + test_item == 8
