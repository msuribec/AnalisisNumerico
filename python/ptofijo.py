import sympy as sp

#INPUT

def puntofijo(x,f,g,x0,nIterations,tolerance):
    # METHOD SETUP
    fx = f.subs(x, x0)  # f(x0) [Evaluating]
    cont = 0
    err = tolerance + 1
    inicial=x0
    # ITERATING
    while (fx != 0 and err > tolerance and cont < nIterations):
        print("i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
              .format(cont, float(x0), float(fx), float(err)), end="")
        xn = g.subs(x, x0)
        fx = f.subs(x, xn)
        err = abs(xn - x0)
        x0 = xn
        cont = cont + 1
    print("i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
          .format(cont, float(x0), float(fx), float(err)), end="")
    if (fx == 0):
        print(x0, "Es raíz")
    else:
        if (err <= tolerance):
            print(float(x0), "Es aproximación a una raíz con una tolerancia de,", tolerance)
        else:
            print("El método fracasó con", nIterations, "iteraciones")
    sp.plot(f, (x, inicial, x0 + nIterations * tolerance))