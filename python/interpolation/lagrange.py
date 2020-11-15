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


def lagrange_pol(x,y):
    n = len(x)
    poly = n * [0.0]
    for i in range(n):
        p = 1.0
        #Denominators Prod_{j != i} (x_i - x_j)
        for j in (j for j in range(n) if (j != i)):
            p *= (x[i] - x[j])
        # Compute y_i/Prod_{j != i} (x_i - x_j)
        p = y[i] / p
        term = [p] + (n - 1) * [0]
        # Compute term := p*Prod_{j != i} (x - x_j)
        for j in (j for j in range(n) if (j != i)):
            for k in range(n - 1, 0, -1):
                term[k] += term[k - 1]
                term[k - 1] *= (-x[j])
        coef=y[i]
        newList = []
        for elem in term:
            newList.append(elem /coef)

        print("L("+str(i)+")")

        print(newList)
        print(str(coef)+"*L(" + str(i) + ")")
        for j in range(n):
            poly[j] += term[j]
        print(term)
    print("")
    print("Coeficientes del Polinomio")
    print(poly)
    return poly


def lagrange_polGUI(x, y,Scrolledtext1):
    n = len(x)
    poly = n * [0.0]
    for i in range(n):
        p = 1.0
        # Denominators Prod_{j != i} (x_i - x_j)
        for j in (j for j in range(n) if (j != i)):
            p *= (x[i] - x[j])
        # Compute y_i/Prod_{j != i} (x_i - x_j)
        p = y[i] / p
        term = [p] + (n - 1) * [0]
        # Compute term := p*Prod_{j != i} (x - x_j)
        for j in (j for j in range(n) if (j != i)):
            for k in range(n - 1, 0, -1):
                term[k] += term[k - 1]
                term[k - 1] *= (-x[j])
        coef = y[i]
        newList = []
        for elem in term:
            newList.append(elem / coef)
        Scrolledtext1.insert(tk.INSERT, "L(" + str(i) + ")=")
        Scrolledtext1.insert(tk.INSERT, newList)
        Scrolledtext1.insert(tk.INSERT, "\n"+ str(coef) + "*L(" + str(i) + ")=")
        Scrolledtext1.insert(tk.INSERT, term)
        Scrolledtext1.insert(tk.INSERT, "\n")

        for j in range(n):
            poly[j] += term[j]

    Scrolledtext1.insert(tk.INSERT, "")

    Scrolledtext1.insert(tk.INSERT, "The coefficients are: \n")

    Scrolledtext1.insert(tk.INSERT, poly)
    return poly
# if __name__ == "__main__":
#     x = [-1, 1, 2, 4 ]
#     y = [7, -1, -8, 2]
#     lagrange_pol(x,y)