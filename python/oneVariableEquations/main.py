"""
Metodos numericos en Anaconda Python3.8.
Author: Equipo analisis numerico
"""

import sympy as sp
import oneVariableEquations.bisection as bisection
import oneVariableEquations.busquedasInc as busquedasInc
import oneVariableEquations.newton as newton
import oneVariableEquations.ptofijo as ptofijo
import oneVariableEquations.raicesmult as raicesmult
import oneVariableEquations.reglaFalsa as reglaFalsa
import oneVariableEquations.secant as secant

# x=Symbol("x")
# f=eval(input("Ingrese la función f(x). Por ejemplo: exp(-x)-x\n"))
# x0=float(input("Ingrese el valor inicial\n"))
# nIterations=int(input("Ingrese el número máximo de iteraciones\n"))
# tolerance=float(input("Ingrese la tolerancia\n"))
#

def run_example_busquedasIncrementales():
    print("\n\n Solucion: Busquedas incrementales")
    x=sp.Symbol('x')
    f=x ** 3 - 7.51 * x ** 2 + 18.4239 * x - 14.8331
    tol = 0.05
    iter_max = 100
    x0 = 0
    busquedasInc.busquedasIncrementales(x,f, x0, tol, iter_max)


def run_example_RegFalsi():
    x = sp.Symbol('x')
    f = x ** 3 - 7.51 * x ** 2 + 18.4239 * x - 14.8331
    xin = 3
    xs = 3.5
    tolerancia = 0.0005
    iteraciones = 100
    reglaFalsa.reglaFalsa(x,f,xin,xs,tolerancia,iteraciones)

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

    x = sp.Symbol('x')
    f = x ** 3 - 7.51 * x ** 2 + 18.4239 * x - 14.8331
    tol = 0.05
    iter_max = 50
    a = 3.0
    b = 3.5
    bisection.bisection(x,f, a, b, tol, iter_max)


def run_example_ptofijo():
    x = sp.Symbol('x')
    x = sp.Symbol('x')
    f = sp.exp(-x) - x
    g= sp.exp(-x)

    x0=0
    nIterations=100
    tolerance=0.006

    ptofijo.puntofijo(x,f,g,x0, nIterations,tolerance)


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
    f=sp.exp(-x) - x
    tol = 0.05
    iter_max = 100
    x0 = 0.0
    newton.newton(x,f, x0, tol, iter_max)

def run_example_secant():
    print("\n\nSolucion: Secant")

    x = sp.Symbol('x')
    f=sp.exp(-x) - x
    tol = 0.0005
    iter_max = 100
    x0 = 0.0
    x1 = 1.0
    secant.secant(x,f, x0, x1,iter_max,tol)


def run_example_raices():
    x = sp.Symbol('x')
    f=(x-24)**4+3
    x0=0
    nIterations=100
    tolerance=0.0005

    raicesmult.rmult(x, f, x0, nIterations, tolerance)

def main():
    """Ejecuta todos los ejemplos"""
    #run_example_busquedasIncrementales()
    #run_example_bisection()

    #run_example_RegFalsi()

    #run_example_newton()
    #run_example_ptofijo()
    #run_example_raices()
    #run_example_secant()


if __name__ == '__main__':
    main()
