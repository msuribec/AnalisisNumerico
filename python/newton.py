def newton(f, df, x0, tol, n):
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
    fx= f(x0)
    dfx= df(x0)
    er = tol + 1
    i=0


    while fx!=0 and er>tol and i<n and dfx!=0:
        x1 = x0 - (fx/dfx)
        fx= f(x1)
        dfx= df(x1)
        er= abs(x1 - x0)
        x0=x1
        i=i+1

        print("i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
              .format(i, x0, fx, er ), end="")

        if fx== 0:
            print(x0, "Es raíz")
        elif er <= tol:
            print(x1, ' es aproximación a una raíz con tolerancia ', tol)
        elif dfx == 0:
            print(x1, ' es una posible raíz multiple')
        else:
            print('El método fracasó con ', i, ' iteraciones.')


