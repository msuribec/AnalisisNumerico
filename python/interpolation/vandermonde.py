
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

import numpy as np

def vanderMonde(x,y):
    V=makeVandermondeMatrix(x)
    i=0
    for line in V:
        print(line,end='')
        print('[%f] '%y[i])
        i=i+1
    print('The coefficients for the polynomial in descending order are )')
    sol=np.linalg.solve(np.array(V),np.array(y))
    print(sol)
    return sol

def makeVandermondeMatrix(x):
    grado = len(x) - 1
    len_x = len(x)
    V = []
    for i in range(len_x):
        V += [[0] * len_x]
    for i in range(len_x):
        for j in range(len_x):
            V[i][j] = x[i] ** (grado - j)
    return V

def vanderMondeGUI(x,y,Scrolledtext1):
    Scrolledtext1.insert(tk.INSERT, 'The vandermonde system is :\n')
    V=makeVandermondeMatrix(x)
    i=0
    for line in V:
        Scrolledtext1.insert(tk.INSERT, np.array(line))
        Scrolledtext1.insert(tk.INSERT, '[' + str(y[i]) + ']\n')
        i=i+1
    Scrolledtext1.insert(tk.INSERT, 'The polynomial is:\n')
    sol=np.linalg.solve(np.array(V),np.array(y))
    grado = len(x) - 1
    k=0
    for elem in sol:
        if grado-k==0:
            Scrolledtext1.insert(tk.INSERT, '%.15f'%elem)
        else:
            Scrolledtext1.insert(tk.INSERT, '%.15f x^%d   +  ' % (elem, grado - k))

        k=k+1


# if __name__ == '__main__':
#     # x = [-2.0, -1.0, 2.0,3.0]
#     # y = [12.13533528,6.367879441,-4.610943901,2.085536923]
#     x = [1.0, 2.0, 3.0]
#     y = [1.0 ,4.0 ,9.0]
#     vanderMonde(x,y)
