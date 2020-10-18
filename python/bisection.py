import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
def bisection(x,f, a, b, tol, iter_max):
    """
    Calculates the root of an equation by Bisection method
    Parameters:
            f: Function f(x)
            a: Lower limit
            b: Upper limit
          tol: Tolerance
     iter_max: Maximum number of iterations
    Outpus:
         root: Root value
         iter: Used iterations
    converged: Found the root
    """

    sp.plot(f, (x, a, b))

    fa = f.subs(x,a)
    fb = f.subs(x,b)
    if  fa == 0:
        print (a,' es raíz.')
    else:
        if fa * fb > 0:
            raise ('La función tiene el mismo signo en a y en b. ')
        else:
            i=1
            xm = (a + b) / 2
            fxm = f.subs(x,xm)
            er = b - a
            while i < iter_max and er > tol and fxm != 0:
                print("i: {:03d} xi: {:+.10f} xm: {:+.10f} xf: {:+.10f} f(xi): {:+.10f} f(xm): {:+.10f} f(xf): {:+.10f} eabs: {:+.10f}\n"
                .format(i, float(a), float(fa), float(xm), float(fxm), float(b), float(fb), float(er)), end="")
                if fxm == 0.0: # % solved the equation exactly
                    a = xm
                    b = xm
                    break #% jumps out of the for loop
                    # % decide which half to keep , so that the signs at the ends differ
                if fa * fxm < 0:
                    b = xm
                    fb = fxm
                else:
                    a = xm
                    fa =fxm
                xm = ( a + b )/2
                fxm = f.subs(x,xm)
                er = abs(b-a)
                i = i+1
            print("i: {:03d} xi: {:+.10f} xm: {:+.10f} xf: {:+.10f} f(xi): {:+.10f} f(xm): {:+.10f} f(xf): {:+.10f} eabs: {:+.10f}\n"
                .format(i, float(a), float(fa), float(xm), float(fxm), float(b), float(fb), float(er)), end="")

            if fxm == 0:
                print (xm,' es raíz.')
                converged = True
            else:
                if er < tol:
                    print (xm,' es aproximación a una raíz con tolerancia ', tol)
                    converged = True
                else:
                    print ('El método fracasó con ', i, ' iteraciones.')

