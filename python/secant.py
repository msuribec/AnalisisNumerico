import sympy as sp


def secant(x, f, x0, x1, n, tol):
    fx0 = f.subs(x, x0)

    inicial = x0
    if fx0 == 0:
        print(float(x0), "Es raíz")
    else:
        fx1 = f.subs(x, x1)
        df = sp.diff(f, x)
        i = 0;
        er = tol + 1
        den = fx1 - fx0
        while er > tol and fx1 != 0 and den != 0 and i < n:
            print("i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} den: {:.10f}\n"
                  .format(i + 1, float(x1), float(fx1), float(er),float(den)), end="")
            x2 = x1 - fx1 * (x1 - x0) / den
            er = abs(x2 - x1)
            x0 = x1
            fx0 = fx1
            x1 = x2
            fx1 = f.subs(x, x1)
            den = fx1 - fx0
            i = i + 1
        print("i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
              .format(i + 1, float(x1), float(fx1), float(er)), end="")
        if fx1 == 0:
            print(float(x1), "Es raíz")
        elif er < tol:
            print(float(x1), ' es aproximación a una raíz con tolerancia ', tol)
        elif den == 0:
            print(float(x1), ' es una posible raíz multiple')
        else:
            print('El método fracasó con ', i, ' iteraciones.')
        sp.plot(f, (x, inicial, x1 + n * tol))
