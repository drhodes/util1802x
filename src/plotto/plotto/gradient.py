import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

class Gradient:
    def __init__(self):
        self.x = None
        self.y = None
        self.gradx = None
        self.grady = None
        
    def compute(self, func, args, xs=(-10, 10), ys=(-10, 10), spacing=1, size=10):
        # control the extent of the x and y axis
        x = np.arange(xs[0], xs[1], spacing)  
        y = np.arange(ys[0], ys[1], spacing)  

        grad = (func.diff(args[0]), func.diff(args[1]))
        gradx, grady = [], []

        for j in y:    
            rowx, rowy = [], []        
            for i in x:    
                argmap = {args[0]:i, args[1]:j}
                rowx.append(float((grad[0].subs(argmap))))
                rowy.append(float((grad[1].subs(argmap))))            
            gradx.append(rowx)
            grady.append(rowy)

        self.x = x
        self.y = x
        self.gradx = gradx
        self.grady = grady

    def is_ready(self):
        # check if data is ready for plotting.
        return self.x != None # todo make this better.
        
    def plot(self, plotter):
        plotter.quiver(self.x, self.y, self.gradx, self.grady)


        

def plot_gradient(func, args, xs=(-10, 10), ys=(-10, 10), spacing=1, size=10):
    # control the extent of the x and y axis
    x = np.arange(xs[0], xs[1], spacing)  
    y = np.arange(ys[0], ys[1], spacing)  

    # change the next line to match your function
    grad = gradient(func, args)
    gradx, grady = [], []

    for j in y:    
        rowx, rowy = [], []        
        for i in x:    
            argmap = {args[0]:i, args[1]:j}
            rowx.append(float((grad[0].subs(argmap))))
            rowy.append(float((grad[1].subs(argmap))))            
        gradx.append(rowx)
        grady.append(rowy)
        
    # control the plot size 
    plt.figure(figsize=(size,size))
    plt.quiver(x, y, gradx, grady)
    return plt

# def test1():
#     # User facing code, three lines.
#     x, y = sp.symbols("x, y")
#     z = x**2 + y**2
#     plot_gradient(z, [x, y], xs=(-2, 2), ys=(-2, 2), spacing=.2)
# test1()    


