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
    
#INPUT


def rmult(x,f,x0,nIterations,tolerance,Scrolledtext1):
    # METHOD SETUP

    fx = f.subs(x, x0)  # f(x0) [Evaluating]
    fp = f.diff(x)  # f'(x)
    fpx = fp.subs(x, x0) # f'(x0) [Evaluating]
    fpp = fp.diff(x)  # f''(x)
    fppx = fpp.subs(x, x0)  # f''(x0) [Evaluating]
    cont = 1
    # Scrolledtext1.insert(tk.INSERT,f)
    # Scrolledtext1.insert(tk.INSERT,fx)
    # Scrolledtext1.insert(tk.INSERT,fp)
    # print (fpx)
    # Scrolledtext1.insert(tk.INSERT,fpp)
    # Scrolledtext1.insert(tk.INSERT,fppx)
    denominator = (fpx ** 2) - (fx * fppx)
    err = tolerance + 1
    inicial=x0
    nCurrent = 0
    Scrolledtext1.insert(tk.INSERT,". . .")
    # ITERATING
    while denominator != 0 and fx != 0 and err > tolerance and cont < nIterations:
        Scrolledtext1.insert(tk.INSERT,"i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
              .format(cont,float(x0) , float(fx), float(err)))
        x1 = x0 - (fx * fpx) / denominator
        fx = f.subs(x, x1)
        fpx = fp.subs(x, x1)
        fppx = fpp.subs(x, x1)
        denominator = (fpx ** 2) - (fx * fppx)
        err = abs(x1 - x0)
        x0 = x1
        cont = cont + 1
    Scrolledtext1.insert(tk.INSERT,"i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
          .format(cont, float(x0), float(fx), float(err)))
    # RESULT
    if (fx == 0):
        Scrolledtext1.insert(tk.INSERT, "%f Es una raíz"%x0)
    else:
        if (err < tolerance):
            Scrolledtext1.insert(tk.INSERT,"%f Es aproximación a una raíz con tolerancia de %f"%(x1,tolerance))
        else:
            if (denominator == 0):
                Scrolledtext1.insert(tk.INSERT,"Se encontró una división por 0")
            else:
                Scrolledtext1.insert(tk.INSERT,"El método fracasó brutalmente con %d iteraaciones" %nIterations)

    sp.plot(f, (x, inicial, x0 + nIterations * tolerance))