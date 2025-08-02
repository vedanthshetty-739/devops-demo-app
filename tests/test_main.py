# test/test_main.py
import pytest
from main import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 2) == -2


# def test_demo():
#     assert 1 != 1
