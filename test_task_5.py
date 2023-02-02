import pytest

from task_5 import Item

def test_insect():
    pencil = Item()
    pencil.set_type('pencil')
    pencil.set_original_price(2.3)
    pencil.raise_price(0.3)
    pencil.raise_price(0.3)
    assert pencil.set_type == 'pencil'
    assert pencil.set_original_price == 2.3
    assert pencil.raised_price == 2.6
