import pytest
from src.calculator import add, subtract, multiply

def test_addition():
    assert add(2, 3) == 5

def test_subtraction():
    assert subtract(5, 3) == 2

def test_multiplication():
    assert multiply(2, 3) == 6

def test_addition_negative():
    assert add(-1, -1) == -2

def test_addition_zero():
    assert add(0, 5) == 5

def test_subtraction_negative():
    assert subtract(-1, -1) == 0

def test_subtraction_zero():
    assert subtract(5, 0) == 5

def test_multiplication_negative():
    assert multiply(-1, 1) == -1

def test_multiplication_zero():
    assert multiply(0, 5) == 0