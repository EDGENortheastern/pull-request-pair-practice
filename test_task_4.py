import pytest

from task_4 import Insect

def test_insect():
    grasshopper_lala = Insect()
    grasshopper_lala.set_type('grasshopper')
    grasshopper_lala.set_name('Lala')
    grasshopper_lala.set_age(4)
    assert grasshopper_lala.type == 'grasshopper'
    assert grasshopper_lala.name == 'Lala'
    assert grasshopper_lala.age == 4
