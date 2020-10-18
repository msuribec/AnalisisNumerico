import sympy as sp
def secant(x,f,x0,x1,n,tol):
    fx0=f.subs(x,x0)
    inicial =x0
    if fx0 == 0:
        print(float(x0), "Es raíz")
    else:
        fx1 = f.subs(f, x1)
        df = sp.diff(f,x)
        dfx = df.subs(df, x0)
        i = 0;
        er = tol + 1
        den = fx1 - fx0
        while er > tol and fx1!=0 and den!=0 and i < n:
            x2 = x1 - fx1 * (x1 - x0) / den
            er = abs(x2 - x1)
            x0 = x1
            fx0 = fx1
            x1 = x2
            fx1 = f.subs(f, x1)
            den = fx1 - fx0
            i = i + 1
        if fx1 == 0:
            print(float(x1), "Es raíz")
        elif er < tol:
            print(float(x1), ' es aproximación a una raíz con tolerancia ', tol)
        elif den == 0:
            print(float(x1), ' es una posible raíz multiple')
        else:
            print('El método fracasó con ', i, ' iteraciones.')
        sp.plot(f, (x, inicial, x1 + n * tol))