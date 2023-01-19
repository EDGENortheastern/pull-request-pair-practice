import pytest

from task_1 import original_price

def test_original_price_basic():
    assert original_price(75,25) == 100.00
    assert original_price(25,75) == 100.00

def test_original_price_fractions():
    assert original_price(458.2,17.13) == 552.91
    assert original_price(373.85,11.2) == 421.00

