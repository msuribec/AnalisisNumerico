import numpy as np
import matplotlib.pyplot as plt
def busquedasIncrementales(f, x0, tol, n):
    fx = f(x0)
    if fx == 0:
        print(x0,' es raíz.')
    else:
        x1 = x0 + tol
        fx1 = f(x1)
        i = 1
        print("i: {:03d}\t x: {:+.10f} x1: {:+.10f} fx: {:+.10f} fx1: {:+.10f} fx*fx1: {:+.10f}\n"
              .format(i, x0, x1, fx, fx1, fx * fx1), end="")
        while fx * fx1 != 0 and fx * fx1 > 0 and i < n:
            x0 = x1
            fx = fx1
            x1 = x0 + tol
            fx1 = f(x1)
            i = i + 1
            print("i: {:03d}\t x: {:+.10f} x1: {:+.10f} fx: {:+.10f} fx1: {:+.10f} fx*fx1: {:+.10f}\n"
              .format(i, x0, x1, fx, fx1, fx * fx1), end="")
        if fx * fx1 == 0:
            if fx == 0:
                print(x0, ' es raíz.')
            else:
                print(x1, ' es raíz.')
        elif fx * fx1 < 0:
            print ('Hay una raíz entre ',x0,' y ',x1, ', iteracion ==>>',i)
        else:
            print('El método fracasó con ', iter_max, ' iteraciones.')

        x = np.arange(x0, x1 + n * tol, tol)
        y = f(x)

        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Solucion: Busquedas incrementales')
        plt.grid()
        plt.show()
