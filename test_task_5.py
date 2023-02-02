import pytest

from task_5 import Item

def test_insect():
    pencil = Item()
    pencil.set_type('pencil')
    pencil.set_original_price(2.3)
    pencil.raise_price(0.3)
    assert pencil.type == 'pencil'
    assert pencil.original_price == 2.3
    assert pencil.price == 2.6
    assert pencil.get_cost_of_10() == 26
