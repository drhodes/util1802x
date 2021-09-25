from .vector import Vec

class Func:
    def __init__(self, freevars, expr):
        self.freevars = freevars
        self.expr = expr

    def grad(self):
        return Vec([self.expr.diff(var) for var in self.freevars])
        
    
