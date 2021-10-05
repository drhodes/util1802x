import sympy
import pytest
from pyquchk import qc

from util1802x import Func, Vec

def test_gradient():
    x, y = vars = sympy.symbols("x y")
    f = Func(vars, x**2 + y**2)
    assert f.grad() == Vec([2*x, 2*y])


    
