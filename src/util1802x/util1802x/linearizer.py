# Copyright 2021, @stalcod15

import sympy

class SystemSolver:
    '''
    This class utilizes the sympy library to solve multivariate
    systems of equations
    '''
    def __init__(self, ind_variables, dep_variables, functions):
        '''
        ind_variables: tuple/list containing independent variables (sympy symbols)
        dep_variables: tuple/list containing dependent variables (sympy symbols)
        functions: tuple/list containing the functions in the system of equations
            ex: variables = (x,y) -> functions = (x+y, x/y)
        '''
        self.ind_variables = sympy.Matrix(ind_variables) 
        self.dep_variables = sympy.Matrix(dep_variables) 
        self.functions = sympy.Matrix(functions)
        
    def get_ind_variables(self):
        return self.ind_variables
    
    def get_dep_variables(self):
        return self.dep_variables
    
    def get_functions(self):
        return self.functions
    
    def Evaluate(self, p0):
        '''
        Evaluates the system of equations at p0
        p0: list/tuple containing coordinates of a point
            Note: be sure coordinates are ordered in the same manner as the variables vector
            ie: if self.variables = (x,y) -> p0 = (x0,y0), not (y0,x0)
        '''
        return self.functions.subs(dict(zip(self.ind_variables, p0)))
    
    def Jacobian(self):
        '''
        Computes Jacobian for the system of equations
        '''
        return sympy.Matrix([[fun.diff(i) for i in self.ind_variables] for fun in self.functions])

class Linearizer(SystemSolver):
    def Linearize(self, p0):
        '''
        Linearizes the system of equations at point p0
        p0: list/tuple containing coordinates of a point
            Note: be sure coordinates are ordered in the same manner as the variables vector
            ie: if self.variables = (x,y) -> p0 = (x0,y0), not (y0,x0)
        '''
        return self.Jacobian().subs(dict(zip(self.ind_variables, p0)))
    
    def Solve(self, p0, delta):
        '''
        Returns the changes to the output vector given known changes to the inputs
        p0: list/tuple containing coordinates of a point
            Note: be sure coordinates are ordered in the same manner as the variables vector
            ie: if self.variables = (x,y) -> p0 = (x0,y0), not (y0,x0)
        delta: list/tuple containing changes in independent variables
                Note: be sure changes are ordered in the same manner as the variables vector
                ie: if self.ind_variables = (x,y) -> inputs = (dx,dy), not (dy,dx)
        '''
        return self.Linearize(p0) * self.ind_variables.subs(dict(zip(self.ind_variables, delta)))
    
    def SolveInv(self, p0, delta):
        '''
        Returns the changes to the input vector given known changes to the outputs
        p0: list/tuple containing coordinates of a point
            Note: be sure coordinates are ordered in the same manner as the variables vector
            ie: if self.variables = (x,y) -> p0 = (x0,y0), not (y0,x0)
        delta: list/tuple containing changes in dependent variables
                Note: be sure changes are ordered in the same manner as the variables vector
                ie: if self.dep_variables = (a,b) -> outputs = (da,db), not (db,da)
        '''
        try:
            return self.Linearize(p0).inv() * self.dep_variables.subs(dict(zip(self.dep_variables, delta)))
        except Exception as e:
            return e.args[0]

        
