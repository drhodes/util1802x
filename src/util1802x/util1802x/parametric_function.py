# Parametric function with one free variable
import sympy as sp
from util1802x import Vec


class ParametricFunc():
    def __init__(self, freevar: sp.Symbol, functions: Vec):
        self.freevar = freevar
        self.functions = functions

    def diff(self):
        return ParametricFunc(self.freevar, self.functions.diff(self.freevar))

    def __eq__(self, other):
        funcs = other.functions.subs(other.freevar, self.freevar)
        return self.functions == funcs

    def norm(self):
        # the magnitude of this parametric function
        return sp.sqrt(self.functions.dot(self.functions))

    
