import sympy as sp

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



def newton(x,f, x0, tol, n,Scrolledtext1):
    """
    Calculates the root of an equation by Newton method
    Parameters:
            f: Function f(x)
           df: Derivative of function f(x)
           x0: Initial guess
          tol: Tolerance
     iter_max: Maximum number of iterations
    Outpus:
         root: Root value
         iter: Used iterations
    converged: Found the root
    """
    df = sp.diff(f, x)
    fx= f.subs(x,x0)
    dfx= df.subs(x,x0)
    er = tol + 1
    i=0
    inicial=x0
    x1=x0
    while fx!=0 and er>tol and i<n and dfx!=0:
        Scrolledtext1.insert(tk.INSERT,"i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
              .format(i, float(x0), float(fx), float(er)))
        x1 = x0 - (fx/dfx)
        fx= f.subs(x,x1)
        dfx= df.subs(x,x1)
        er= abs(x1 - x0)
        x0=x1
        i=i+1

    Scrolledtext1.insert(tk.INSERT,"i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
          .format(i, float(x0), float(fx), float(er)))

    if fx== 0:
        Scrolledtext1.insert(tk.INSERT,"%x0 Es raíz"%x0)
    elif er <= tol:
        Scrolledtext1.insert(tk.INSERT,' %f es aproximación a una raíz con tolerancia %f' %(x1,tol))
    elif dfx == 0:
        Scrolledtext1.insert(tk.INSERT,'%f es una posible raíz multiple'%x1)
    else:
        Scrolledtext1.insert(tk.INSERT,'El método fracasó con %d iteraciones' % i)

    sp.plot(f, (x, inicial, x0 + n * tol))