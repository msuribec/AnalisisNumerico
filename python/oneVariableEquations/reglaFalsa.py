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

def reglaFalsa(x,f,xin,xs,tolerancia,iteraciones,Scrolledtext1):
    sp.plot(f, (x, xin, xs))

    fxin = f.subs(x,xin)
    fxs = f.subs(x,xs)
    if fxin == 0:
        Scrolledtext1.insert(tk.INSERT,"\n %f Es raiz"%xin)
    elif fxs == 0:
        Scrolledtext1.insert(tk.INSERT,"%\nf Es raiz"%xs)
    elif (fxin * fxs < 0 ):
        xmedio = xin - ((fxin * (xs-xin))/(fxs -fxin))
        n = 1
        fxmedio = f.subs(x,xmedio)
        err = tolerancia +1

        Scrolledtext1.insert(tk.INSERT,'\n{:30} {:30} {:30} {:30} {:30}\n'.format('iter', 'xin', 'xmedio', 'fxm', 'err'))
        Scrolledtext1.insert(tk.INSERT,'\n{:30} {:30} {:30} {:30} {:30}\n'.format(str(n - 1), str(xin), str(xmedio), str(fxmedio), str(err)))
        while(err > tolerancia ) and (fxmedio != 0) and (n < iteraciones):
            if fxin * fxmedio <0:
                xs = xmedio
                fxs = fxmedio
            else:
                xin = xmedio
                fxin = fxmedio
            temp = xmedio
            xmedio = xin - ((fxin * (xs-xin))/(fxs -fxin))
            fxmedio = f.subs(x,xmedio)
            err = abs(xmedio - temp)
            n = n + 1

            Scrolledtext1.insert(tk.INSERT,'\n{:30} {:30} {:30} {:30} {:30}\n'.format(str(n), str(xin), str(xmedio), str(fxmedio), str(err)))
        if fxmedio == 0:
            Scrolledtext1.insert(tk.INSERT," \n%.15f es raiz "%xmedio)
        elif err< tolerancia:
            Scrolledtext1.insert(tk.INSERT," \n%.15f es una raiz aproximada con tolerancia de = %f" %(xmedio,tolerancia) )
        else:
            Scrolledtext1.insert(tk.INSERT,"\nFallo con" + str(iteraciones) + " iteraciones.\n")
    else:
        Scrolledtext1.insert(tk.INSERT,"\nIntervalo inadecuado.\n")