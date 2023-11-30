import pytest

from src.keyboard import Keyboard


@pytest.fixture()
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_init(kb):
    name, price, num, lang = kb.name, kb.price, kb.quantity, kb.language
    assert f"{name} {price} {num} {lang}" == "Dark Project KD87A 9600 5 EN"


def test_str(kb):
    assert str(kb) == "Dark Project KD87A"


def test_change_lang(kb):
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"
    with pytest.raises(AttributeError):
        kb.language = 'CH'
