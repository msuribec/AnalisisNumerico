import sympy as sp

#INPUT


def rmult(x,f,x0,nIterations,tolerance):
    # METHOD SETUP

    fx = f.subs(x, x0)  # f(x0) [Evaluating]
    fp = f.diff(x)  # f'(x)
    fpx = fp.subs(x, x0) # f'(x0) [Evaluating]
    fpp = fp.diff(x)  # f''(x)
    fppx = fpp.subs(x, x0)  # f''(x0) [Evaluating]
    cont = 1
    # print(f)
    # print(fx)
    # print(fp)
    # print (fpx)
    # print(fpp)
    # print(fppx)
    denominator = (fpx ** 2) - (fx * fppx)
    err = tolerance + 1
    inicial=x0
    nCurrent = 0
    print(". . .")
    # ITERATING
    while denominator != 0 and fx != 0 and err > tolerance and cont < nIterations:
        print("i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
              .format(cont,float(x0) , float(fx), float(err)), end="")
        x1 = x0 - (fx * fpx) / denominator
        fx = f.subs(x, x1)
        fpx = fp.subs(x, x1)
        fppx = fpp.subs(x, x1)
        denominator = (fpx ** 2) - (fx * fppx)
        err = abs(x1 - x0)
        x0 = x1
        cont = cont + 1
    print("i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
          .format(cont, float(x0), float(fx), float(err)), end="")
    # RESULT
    if (fx == 0):
        print(float(x0), "Es una raíz")
    else:
        if (err < tolerance):
            print(float(x1), "Es aproximación a una raíz con tolerancia de", tolerance)
        else:
            if (denominator == 0):
                print("Se encontró una división por 0")
            else:
                print("El método fracasó brutalmente con", nIterations, "iteraciones")

    sp.plot(f, (x, inicial, x0 + nIterations * tolerance))