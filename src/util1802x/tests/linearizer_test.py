'''
otools: Test module.

Meant for use with py.test.
Write each test as a function named test_<something>.
Read more here: http://pytest.org/

Copyright 2021, participants of 18.02x
Licensed under MIT
'''
import sympy
import math
import pytest
from pyquchk import qc

from util1802x.linearizer import Linearizer, SystemSolver

# for testing equality between IEEE floats
def isclose(a, b): assert(math.isclose(a, b))

# python requires that we name operators.
def add(a, b): return a + b
def mul(a, b): return a * b
def power(a, b): return a ** b

# check the quickcheck docs for info on these decorators
# https://github.com/t2y/pytest-quickcheck

@pytest.mark.parametrize("op1", [add, mul])   # pick a random operator
@pytest.mark.parametrize("op2", [mul, power]) # pick another one
@pytest.mark.randomize(min_num=0, max_num=20, ncalls=2) 
def test_jacobian(n: int,    
                  m: int,
                  x0: float,
                  y0: float,
                  op1,
                  op2,
                  ):
    '''
    generate 5186 random functions and check to see if SystemSolver is
    generating the jacobian correctly.
    '''
    x,y,a,b = sympy.symbols("x,y,a,b")

    # generate a random function f from random binary operators
    f = op1(op2(x,n), op2(y,m)) 
    # generate a random function g
    g = op2(2,x) + op1(2,y)

    ind_variables = (x,y)
    dep_variables = (a,b)
    funcs = (f,g)
    solver = SystemSolver(ind_variables, dep_variables, funcs)

    # generate random test point
    p0map = {x:x0, y:y0}
    J = solver.Jacobian().subs(p0map)
    
    # check to see if the Jacobian is what it should be in the 2x2 case.  
    isclose(J[0,0], f.diff(x).subs(p0map))
    isclose(J[0,1], f.diff(y).subs(p0map))
    isclose(J[1,0], g.diff(x).subs(p0map))
    isclose(J[1,1], g.diff(y).subs(p0map))
    
@qc
def test_add(a=int, b=int):
    c=a
    if a < -100000: c = 42
    assert add(a, b) == c + b
