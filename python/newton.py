import sympy as sp
def newton(x,f, x0, tol, n):
    """
    Calculates the root of an equation by Newton method
    Parameters:
            f: Function f(x)
           df: Derivative of function f(x)
           x0: Initial guess
          tol: Tolerance
     iter_max: Maximum number of iterations
    Outpus:
         root: Root value
         iter: Used iterations
    converged: Found the root
    """
    df = sp.diff(f, x)
    fx= f.subs(x,x0)
    dfx= df.subs(x,x0)
    er = tol + 1
    i=0
    inicial=x0
    while fx!=0 and er>tol and i<n and dfx!=0:
        print("i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
              .format(i, float(x0), float(fx), float(er)), end="")
        x1 = x0 - (fx/dfx)
        fx= f.subs(x,x1)
        dfx= df.subs(x,x1)
        er= abs(x1 - x0)
        x0=x1
        i=i+1

    print("i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
          .format(i, float(x0), float(fx), float(er)), end="")

    if fx== 0:
        print(float(x0), "Es raíz")
    elif er <= tol:
        print(float(x1), ' es aproximación a una raíz con tolerancia ', tol)
    elif dfx == 0:
        print(float(x1), ' es una posible raíz multiple')
    else:
        print('El método fracasó con ', i, ' iteraciones.')

    sp.plot(f, (x, inicial, x0 + n * tol))