
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
    
def busquedasIncrementales(x,f, x0, tol, n,Scrolledtext1):

    inicial=x0
    fx = f.subs(x,x0)
    if fx == 0:
        Scrolledtext1.insert(tk.INSERT,' %fes raíz.'%x0)
    else:
        x1 = x0 + tol
        fx1 = f.subs(x,x1)
        i = 1
        Scrolledtext1.insert(tk.INSERT,"i: {:03d}\t x: {:+.10f} x1: {:+.10f} fx: {:+.10f} fx1: {:+.10f} fx*fx1: {:+.10f}\n"
              .format(i, float(x0), float(x1), float(fx), float(fx1), float(fx * fx1)))
        while fx * fx1 != 0 and fx * fx1 > 0 and i < n:
            x0 = x1
            fx = fx1
            x1 = x0 + tol
            fx1 = f.subs(x,x1)
            i = i + 1
            Scrolledtext1.insert(tk.INSERT,"i: {:03d}\t x: {:+.10f} x1: {:+.10f} fx: {:+.10f} fx1: {:+.10f} fx*fx1: {:+.10f}\n"
                  .format(i, float(x0), float(x1), float(fx), float(fx1), float(fx * fx1)))
        if fx * fx1 == 0:
            if fx == 0:
                Scrolledtext1.insert(tk.INSERT,' %f es raíz.'%x0)
            else:
                Scrolledtext1.insert(tk.INSERT, '%f es raíz.'%f)
        elif fx * fx1 < 0:
            Scrolledtext1.insert('Hay una raíz entre '+ str(float(x0)) +' y ' + str(float(x1)) +  ', iteracion ==>>' + str(i))
        else:
            Scrolledtext1.insert(tk.INSERT,'El método fracasó con '+ str(iter_max) +  ' iteraciones.')


        sp.plot(f, (x, inicial, x1 + n * tol))
