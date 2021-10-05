import sympy as sp
import pytest
from pyquchk import qc

from util1802x import ParametricFunc, Func, Vec


def test_pfunc():
    t = sp.Symbol('t')
    pfunc = ParametricFunc(t, Vec([t**2, t**2]))
    assert pfunc.diff() == ParametricFunc(t, Vec([2 * t, 2 * t]))


def test_pfunc_norm():
    t = sp.Symbol('t')
    v = Vec([t**2, t**2])
    vdiff = sp.diff(v, t)
    pfunc = ParametricFunc(t, v)
    assert pfunc.diff().norm() == sp.sqrt(vdiff.dot(vdiff))


def test_pfunc_equality_different_freevars():
    # two functions with different free vars should be equal
    # regardless of free variable.
    t, x = sp.symbols('t x')

    vx = Vec([x**2, x**2])
    vt = Vec([t**2, t**2])
    pfunct = ParametricFunc(t, vt)
    pfuncx = ParametricFunc(x, vx)

    assert pfunct == pfuncx


def test_pfunc_unit_tangent_vector():
    t = sp.symbols('t')
    x = t
    y = -5 * t**2
    func = ParametricFunc(t, Vec([x, y]))
    v = Vec(
        [1 / (sp.sqrt(1 + 100 * t**2)), (-10 * t) / (sp.sqrt(1 + 100 * t**2))])
    testfunc = ParametricFunc(t, v)
    assert func.unit_tangent_vector() == v
