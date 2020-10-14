"""
Metodos numericos en Anaconda Python3.8.
Author: Equipo analisis numerico
"""
import matplotlib.pyplot as plt
import math
import numpy as np
import sympy as sp
import solucionBusBicNew

#from pylab import *

#from sympy.plotting import plot 
#x=Symbol('x') 

#plot(x**2, line_color='red')

#plot( (sin(x),(x, -2*pi, 2*pi)),(cos(x), (x, -pi, pi)))
#sp.plot(sp.sin(x)*sp.log(x))
#sp.plot(sp.sin(2*sp.sin(2*sp.sin(x))))

#int1 = sp.Integral( sp.sin(x)**3 /(2*x), x)
#sp.latex(int1)

def print_var(var_name, value):
    print("{} = {}".format(var_name, value))

def run_example_busquedasIncrementales():
    print("\n\n Solucion: Busquedas incrementales")
    
    def f(x):
        return x**3 - 7.51 * x**2 + 18.4239 * x - 14.8331  
    
    tol = 0.05  
    iter_max = 100
    x = 0
    xInicial = x

    print_var("tolerancia", tol)
    print_var("maximo iteraciones", iter_max)
    print_var("x inicial", x)
    [root, i, converged,x,x1] = solucionBusBicNew.busquedasIncrementales(f, x, tol, iter_max)
    print_var("Raiz", root)
    print_var("iteracion", i)
    print_var("converge", converged)

    x = np.arange(xInicial,x1 + iter_max * tol )
    y = x**3 - 7.51 * x**2 + 18.4239 * x - 14.8331   

    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solucion: Busquedas incrementales')
    plt.grid()
    plt.show()

def run_example_bisection():
    print("\n\n Solution: Biseccion")
    # Bisection method (find roots of an equation)
    #   Pros:
    #       It is a reliable method with guaranteed convergence;
    #       It is a simple method that does the search of the root by means of
    #           a binary search;
    #       There is no need to calculate the derivative of the function.
    #   Cons:
    #       Slow convergence;
    #       It is necessary to enter a search interval [a, b];
    #       The interval reported must have a signal exchange, f (a) * f (b)<0.

    def f(x):
        return x**3 - 7.51 * x**2 + 18.4239 * x - 14.8331 
        
    tol = 0.05  
    iter_max = 50
    a = 3.0
    b = 3.5
    print_var("tolerancia", tol)
    print_var("maximo iteraciones", iter_max)
    print_var("a", a)
    print_var("b", b)
    [root, i, converged, fa, xm, fxm, fb, er] = solucionBusBicNew.bisection(f, a, b, tol, iter_max)
    print_var("Raiz", root)
    print_var("iteracion", i)
    print_var("converge", converged)

    x = np.arange(a , fxm + iter_max * tol  )
    y = x**3 - 7.51 * x**2 + 18.4239 * x - 14.8331 

    plt.plot(x,y,tol)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solucion: Biseccion')
    plt.grid()
    plt.show()

def run_example_newton():
    print("\n\nSolucion: Newton")
    # Newton method (find roots of an equation)
    #   Pros:
    #       It is a fast method.
    #    Cons:
    #       It may diverge;
    #       It is necessary to calculate the derivative of the function;
    #       It is necessary to give an initial x0 value where
    #           f'(x0) must be nonzero.

    import sympy as sp 
    x = sp.Symbol('x') 
    y = sp.exp(-x)-x  

    print(sp.diff(y,x))  #calcula la 1a derivada 
    #print(sp.diff(y,x,2)) #calcula la 2a derivada 
    #print(sp.diff(y,x,3)) #calcula la 3a derivada 
    #print(sp.diff(y,x,4)) #calcula la 4a derivada 

    def f(x):
        return math.exp(-x)-x

    def df(x):
        return -1 - math.exp(-x)

    tol = 0.05
    iter_max = 100
    x0 = 0.0
    print_var("tolerancia", tol)
    print_var("maximo iteraciones", iter_max)
    print_var("x0", x0)
    [root, i, converged] = solucionBusBicNew.newton(f, df, x0, tol, iter_max)
    print_var("Raiz", root)
    print_var("iteracion", i)
    print_var("converge", converged)

def main():
    """Ejecuta todos los ejemplos"""
    run_example_busquedasIncrementales()
    run_example_bisection()
    run_example_newton()

if __name__ == '__main__':
    main()
