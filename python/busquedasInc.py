import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
def busquedasIncrementales(x,f, x0, tol, n):

    inicial=x0
    fx = f.subs(x,x0)
    if fx == 0:
        print(x0,' es raíz.')
    else:
        x1 = x0 + tol
        fx1 = f.subs(x,x1)
        i = 1
        print("i: {:03d}\t x: {:+.10f} x1: {:+.10f} fx: {:+.10f} fx1: {:+.10f} fx*fx1: {:+.10f}\n"
              .format(i, float(x0), float(x1), float(fx), float(fx1), float(fx * fx1)), end="")
        while fx * fx1 != 0 and fx * fx1 > 0 and i < n:
            x0 = x1
            fx = fx1
            x1 = x0 + tol
            fx1 = f.subs(x,x1)
            i = i + 1
            print("i: {:03d}\t x: {:+.10f} x1: {:+.10f} fx: {:+.10f} fx1: {:+.10f} fx*fx1: {:+.10f}\n"
                  .format(i, float(x0), float(x1), float(fx), float(fx1), float(fx * fx1)), end="")
        if fx * fx1 == 0:
            if fx == 0:
                print(float(x0), ' es raíz.')
            else:
                print(float(x1), ' es raíz.')
        elif fx * fx1 < 0:
            print ('Hay una raíz entre ',float(x0),' y ',float(x1), ', iteracion ==>>',i)
        else:
            print('El método fracasó con ', iter_max, ' iteraciones.')


        sp.plot(f, (x, inicial, x1 + n * tol))
