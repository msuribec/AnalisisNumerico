import numpy as np

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
    
def gausSeidel(A, b,x, tol, iteMax,Scrolledtext1):
    p=spectralRadiusGS(A)
    if p<1:
        n=len(x)
        L = np.tril(A)
        U = A - L
        ite = 1
        norm = tol + 1
        Scrolledtext1.insert(tk.INSERT,"\n|iter|")
        for i in range(n):
            Scrolledtext1.insert(tk.INSERT,"      x{0}    |".format(i))
        Scrolledtext1.insert(tk.INSERT,"   E   |\n")
        while (norm > tol and ite < iteMax):
            xold = x
            x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
            norm = max(abs((x - xold)))
            Scrolledtext1.insert(tk.INSERT,"\n|", str(ite).ljust(2), "|    ")
            for i in x:
                Scrolledtext1.insert(tk.INSERT,"|    %.9f" % i, "|    ")
            Scrolledtext1.insert(tk.INSERT,"    %.1e" % norm, "|\n")

            ite += 1

        if norm <= tol:
            Scrolledtext1.insert(tk.INSERT, '\nThe solution is \n')
            Scrolledtext1.insert(tk.INSERT,x)
            Scrolledtext1.insert(tk.INSERT,'\nSe alcanzó una aproximaxión con tol %.15f\n' % tol)
        else:
            Scrolledtext1.insert(tk.INSERT,'\nEl método fracasó con %d iteraciones\n' % ite)
    else:
        Scrolledtext1.insert(tk.INSERT,'\n The spectral radius of Tj is not less than zero, method will not converge\n')


def spectralRadiusGS(A):
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    D = A + L + U
    aux=np.linalg.inv(D-L)
    Tg = np.matmul(aux,U)
    w, v = np.linalg.eig(Tg)
    p = np.max(np.abs(w))
    return p

def solveGaussSeidel(mat,coef,initial,tol,itemax,Scrolledtext1):
    aux = np.array(mat).astype(float)
    b = np.array(coef).astype(float)
    n = len(mat)
    A = aux.reshape(n, n)
    gausSeidel(A, b, initial, tol, itemax,Scrolledtext1)

# if __name__ == "__main__":
#     tind = [-25, 82, 75, -43]
#     mat = [[45, 13, -4, 8], [-5, -28, 4, -14], [9, 15, 63, -7], [2, 3, -8, -42]]
#     x = [2, 2, 2, 2]
#     solveGaussSeidel(mat,tind,x,1E-7,1000)


