import sympy


class Linearizer:
    '''
    Class for linearizing multivariate systems of equations (requires the sympy library)
    Instructions:
        - Define sympy symbols -> x,y = sympy.symbols("x,y")
        - Define system of equations -> f = f(x,y)
                                        g = g(x,y)
        - Create Linearizer object -> L = Linearizer((x,y), (f,g))
        - Run Jacobian function to get linearization at point p0
        - Use the solve functions to solve the system given known inputs/outputs
    '''
    def __init__(self, system, args_in, args_out=None):
        self.system = system
        self.args_in = args_in
        self.args_out = args_out
        # Changes in input arguments
        self.Delta_input = sympy.Matrix([sympy.symbols('Delta_' + str(arg)) for arg in self.args_in])
        # Changes in output arguments
        if args_out != None:
            self.Delta_output = sympy.Matrix([sympy.symbols('Delta_' + str(arg)) for arg in self.args_out])
    def set_args_out(self, args):
        '''
        Set output arguments. Output arguments must be set before using SolveInv function
        '''
        self.args_out = args
        self.Delta_output = self.Delta_output = sympy.Matrix([sympy.symbols('Delta_' + str(arg)) for arg in self.args_out])
        return
    def Jacobian(self, args):
        '''
        Computes Jacobian for the system of equations at p0
        args: dictionary mapping args to their coordinates 
            ex: If p0 = (1,2), args = {arg_1: 1, arg_2: 2}
        '''
        self.J = sympy.Matrix([[fun.diff(i) for i in self.args_in] for fun in self.system]).subs(args)
        return self.J
    def Solve(self, args):
        '''
        Solves for the output vector given known inputs
        args = dictionary mapping arguments to their respective change
            ex: If change in (arg_1, arg_2) = (1,2), args = dict(zip(self.Delta_input, (1,2)))
        '''
        return self.J * self.Delta_input.subs(args)
    def SolveInv(self, args):
        '''
        Solves for the input vector given known outputs
        args_out must be defined before using SolveInv function
        args = dictionary mapping arguments to their respective change
            ex: If change in (arg_1, arg_2) = (1,2), args = dict(zip(self.Delta_output, (1,2)))
        '''
        return self.J.inv() * self.Delta_output.subs(args)
