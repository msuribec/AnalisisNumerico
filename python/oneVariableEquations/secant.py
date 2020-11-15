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

def secant(x, f, x0, x1, n, tol,Scrolledtext1):
    fx0 = f.subs(x, x0)

    inicial = x0
    if fx0 == 0:
        Scrolledtext1.insert(tk.INSERT," %f Es raíz"%x0)
    else:
        fx1 = f.subs(x, x1)
        df = sp.diff(f, x)
        i = 0;
        er = tol + 1
        den = fx1 - fx0
        while er > tol and fx1 != 0 and den != 0 and i < n:
            Scrolledtext1.insert(tk.INSERT,"i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} den: {:.10f}\n"
                  .format(i + 1, float(x1), float(fx1), float(er),float(den)))
            x2 = x1 - fx1 * (x1 - x0) / den
            er = abs(x2 - x1)
            x0 = x1
            fx0 = fx1
            x1 = x2
            fx1 = f.subs(x, x1)
            den = fx1 - fx0
            i = i + 1
        Scrolledtext1.insert(tk.INSERT,"i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
              .format(i + 1, float(x1), float(fx1), float(er)))
        if fx1 == 0:
            Scrolledtext1.insert(tk.INSERT,float(x1) + "%f Es raíz"%x1)
        elif er < tol:
            Scrolledtext1.insert(tk.INSERT,'%f es aproximación a una raíz con tolerancia %f'%(x1,tol))
        elif den == 0:
            Scrolledtext1.insert(tk.INSERT,'%f es una posible raíz multiple'%x1)
        else:
            Scrolledtext1.insert(tk.INSERT,'El método fracasó con %d iteraciones.'%i)
        sp.plot(f, (x, inicial, x1 + n * tol))
