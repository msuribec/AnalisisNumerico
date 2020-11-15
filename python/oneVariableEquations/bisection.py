import numpy as np
import matplotlib.pyplot as plt

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import sympy as sp
def bisection(x,f, a, b, tol, iter_max,Scrolledtext1):
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
                Scrolledtext1.insert(tk.INSERT,"i: {:03d} xi: {:+.10f} xm: {:+.10f} xf: {:+.10f} f(xi): {:+.10f} f(xm): {:+.10f} f(xf): {:+.10f} eabs: {:+.10f}\n"
                .format(i, float(a), float(fa), float(xm), float(fxm), float(b), float(fb), float(er)))
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
            Scrolledtext1.insert(tk.INSERT,"i: {:03d} xi: {:+.10f} xm: {:+.10f} xf: {:+.10f} f(xi): {:+.10f} f(xm): {:+.10f} f(xf): {:+.10f} eabs: {:+.10f}\n"
                .format(i, float(a), float(fa), float(xm), float(fxm), float(b), float(fb), float(er)))

            if fxm == 0:
                Scrolledtext1.insert(tk.INSERT,' %f es raíz.'%xm)
                converged = True
            else:
                if er < tol:
                    Scrolledtext1.insert(tk.INSERT,'%f es aproximación a una raíz con tolerancia %f' %(xm,tol))
                    converged = True
                else:
                    Scrolledtext1.insert(tk.INSERT,'El método fracasó con ' + str(i) + 'iteraciones.')

