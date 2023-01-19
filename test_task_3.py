import pytest

from task_3 import mystery_func

def test_mystery_func():
    assert mystery_func("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta") == "alpha beta gamma delta"
    assert mystery_func("my cat is my cat fat") == "my cat is fat"
