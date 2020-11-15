import numpy as np
import sympy as sp
from sympy.abc import x


def trapzComp(f, a, b, N=50):
    data = np.linspace(a, b, N + 1)  # N+1 points make N subintervals
    y = f(data)
    y_right = y[1:]  # right endpoints
    y_left = y[:-1]  # left endpoints
    dx = (b - a) / N
    print("h =", dx)
    i = 0
    for line in y:
        print("f(x%d) = %f"%(i,line))
        i = i + 1

    T = (dx / 2) * np.sum(y_right + y_left)
    print("Estimation with composite trapezoid rule is = ", T)
    return T

def simpsComp(f,a,b,N=50):
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    i = 0
    for line in y:
        print("f(x%d) = %f"%(i,line))
        i = i + 1
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    print("Estimation with simpson 1/3 composite method = ", S)

    return S


def simps(f,a,b):
    m=(a+b)/2
    fa=f(a)
    fb=f(b)
    fm=f(m)
    h=(m-a)
    print("with h=%f" %h)
    S = h/3 *(fa+4*fm+fb)
    print("Estimation with simpson 1/3 method = ", S)

    return S

def trapz(f, a, b):
    fa = f(a)
    fb = f(b)
    val = (b - a) * (fa + fb) / 2
    print("Estimation with trapezoid method = ", val)
    return val

def simpson38(f,x0,x3):
    f0=f(x0)
    f3=f(x3)
    h = (x3 - x0) / 3
    x1=x0+h
    x2=x0+2*h
    f1=f(x1)
    f2=f(x2)
    val=(3*h/8)*(f0+3*f1+3*f2+f3)
    print("x0= %f" %x0)
    print("x1= %f" %x1)
    print("x2= %f" % x2)
    print("x3= %f" % x3)
    print("f(x0)= %f" % f0)
    print("f(x1)= %f" % f1)
    print("f(x2)= %f" % f2)
    print("f(x3)= %f" % f3)
    print("Estimation with simpson 3/8 method = ", val)
    return val



if __name__ == '__main__':
    expr = sp.exp(x) - 2 * x
    f = sp.lambdify(x, expr, "numpy")

    trapzComp(f, 1, 2, 10)
    trapz(f, 1, 2)
    simps(f,1,2)
    simpsComp(f, 1, 2, 10)
    simpson38(f,1,2)
