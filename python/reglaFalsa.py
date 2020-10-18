import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def reglaFalsa(x,f,xin,xs,tolerancia,iteraciones):
    sp.plot(f, (x, xin, xs))

    fxin = f.subs(x,xin)
    fxs = f.subs(x,xs)
    if fxin == 0:
        print(float(xin) + " Es raiz")
    elif fxs == 0:
        print(float(xs) + " Es raiz")
    elif (fxin * fxs < 0 ):
        xmedio = xin - ((fxin * (xs-xin))/(fxs -fxin))
        n = 1
        fxmedio = f.subs(x,xmedio)
        err = tolerancia +1

        print('{:30} {:30} {:30} {:30} {:30}'.format('iter', 'xin', 'xmedio', 'fx', 'err'))
        print('{:30} {:30} {:30} {:30} {:30}'.format(str(n - 1), str(xin), str(xmedio), str(fxmedio), str(err)))
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

            print('{:30} {:30} {:30} {:30} {:30}'.format(str(n), str(xin), str(xmedio), str(fxmedio), str(err)))
        if fxmedio == 0:
            print(str(xmedio) + " es raiz ")
        elif err< tolerancia:
            print(str(xmedio) + " es una raiz aproximada con tolerancia de = " + str(tolerancia) )
        else:
            print("Fallo con" + str(iteraciones) + " iteraciones.")
    else:
        print("Intervalo inadecuado.")