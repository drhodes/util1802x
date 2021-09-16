'''
plotto: Test module.

Meant for use with py.test.
Write each test as a function named test_<something>.
Read more here: http://pytest.org/

Copyright 2021, participants of 18.02x
Licensed under MIT
'''

from linearizer import Linearizer
import sympy

def test_example():    
    # 1. Create symbols: ex -> x,y = sympy.symbols("x,y")
    # 2. Create equations: ex -> f = x**2 + 2*y, 
    #                            g = x**4 + 5*y**3 - 1
    # 3. Define args: ex -> args = (x,y)
    # 4. Define system: ex -> system = (f,g)
    # 5. Create Linearizer object: ex -> L = Linearizer(system, args)
    # 6. Run linearize function at point: ex -> L.linearize({x: -4, y: 7})
    x, y = sympy.symbols("x, y")
    f = x**2 + 2*y
    g = x**4 + 5*y**3 - 1
    args = (x, y)
    sys = (f, g)
    L = Linearizer(sys, args)
    print(L.linearize({x: -4, y: 7}))
    assert True

def test_gradient():
    x, y = sympy.symbols("x, y")
    f = x**2 + 2*y
    g = x**4 + 5*y**3 - 1
    args = (x, y)
    sys = (f, g)
    L = Linearizer(sys, args)
    print(L.linearize({x: -4, y: 7}))
    assert True
    
