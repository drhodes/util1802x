import pytest
import random

def add(a, b): return a + b
def mul(a, b): return a * b
def power(a, b): return a ** b

@pytest.fixture
def oper():
    return random.choice([add, mul])
