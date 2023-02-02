import pytest

from task_4 import Insect

def test_person():
    grasshopper_lala = Insect('grasshopper', 'Lala', 4)
    assert(grasshopper_lala.type, 'grasshopper')
    assert(grasshopper_lala.name, 'Lala')
    assert(grasshopper_lala.age, 4)
