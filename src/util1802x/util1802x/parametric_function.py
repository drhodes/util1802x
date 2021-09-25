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
        # TODO: functions should be equal even their free variables
        funcs = other.functions.subs(other.freevar, self.freevar)
        return self.functions == funcs
        # return self.freevar == other.freevar and self.functions == other.functions

    def norm(self):
        # get the norm of self.functions
        return sp.sqrt(self.functions.dot(self.functions))

    
