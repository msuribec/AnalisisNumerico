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

def puntofijo(x,f,g,x0,nIterations,tolerance,Scrolledtext1):
    # METHOD SETUP
    fx = f.subs(x, x0)  # f(x0) [Evaluating]
    cont = 0
    err = tolerance + 1
    inicial=x0
    # ITERATING
    while (fx != 0 and err > tolerance and cont < nIterations):
        Scrolledtext1.insert(tk.INSERT,"i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
              .format(cont, float(x0), float(fx), float(err)))
        xn = g.subs(x, x0)
        fx = f.subs(x, xn)
        err = abs(xn - x0)
        x0 = xn
        cont = cont + 1
    Scrolledtext1.insert(tk.INSERT,"i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
          .format(cont, float(x0), float(fx), float(err)))
    if (fx == 0):
        Scrolledtext1.insert(tk.INSERT,"%f Es raíz"%x0)
    else:
        if (err <= tolerance):
            Scrolledtext1.insert(tk.INSERT," %f Es aproximación a una raíz con una tolerancia de %f"%(x0,tolerance))
        else:
            Scrolledtext1.insert(tk.INSERT,"El método fracasó con % iteraciones" %nIterations)
    sp.plot(f, (x, inicial, x0 + nIterations * tolerance))