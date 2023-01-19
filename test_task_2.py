import pytest

from task_2 import return_middle

def test_return_middle_basic():
    assert return_middle([15, 10, 14]) == 2
    assert return_middle([1, 3, 4]) == 1

def test_return_middle_negatives():
    assert return_middle([-0.410, -23, 4]) == 0
    assert return_middle([-15, -10, 14]) == 1