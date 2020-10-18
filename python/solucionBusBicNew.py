
import math

def busquedasIncrementales(f, x, tol, iter_max):

    converged = False
    i = 0

    fx = f(x)

    if fx == 0:
        print("Verificar: Convergencia.")

    else:
        for i in range(0, iter_max + 1):
            x1 = x + tol
            fx1 = f(x1)
            fx = f(x)

            print("i: {:03d}\t x: {:+.6f} x1: {:+.6f} fx: {:+.6f} fx1: {:+.6f} fx*fx1: {:+.6f}\n"
                    .format(i, x, x1, fx , fx1, fx * fx1), end="")

            if fx * fx1 == 0:
                if fx == 0:
                    converged = True
                    print (x,' es raíz.')
                    break
                else:
                    converged = True
                    print (x1,' es raíz.')
                    break
            else:
                if fx * fx1 < 0:
                    print ('Hay una raíz entre ',x,' y ',x1, ', iteracion ==>>',i)
                    converged = True
                    break

            ndelta_x = x + tol
            x = ndelta_x
        else:
            print ('El método fracasó con ', iter_max,' iteraciones.')
    root = x
    return [root, i, converged,x,x1]

def bisection(f, a, b, tol, iter_max):
    """
    Calculates the root of an equation by Bisection method
    Parameters:
            f: Function f(x)
            a: Lower limit
            b: Upper limit
          tol: Tolerance
     iter_max: Maximum number of iterations
    Outpus:
         root: Root value
         iter: Used iterations
    converged: Found the root
    """
    fa = f(a)
    fb = f(b)
    if  fa == 0:
        print (a,' es raíz.')
    else:
        if fa * fb > 0:
            raise ('La función tiene el mismo signo en a y en b. ')
        else:
            i=1
            xm = (a + b) / 2
            fxm = f(xm)
            er = b - a
            while i < iter_max and er > tol and fxm != 0:
                print("i: {:03d} xi: {:+.10f} xm: {:+.10f} xf: {:+.10f} f(xi): {:+.10f} f(xm): {:+.10f} f(xf): {:+.10f} eabs: {:+.10f}\n"
                .format(i, a, fa, xm, fxm, b, fb, er), end="")
                if fxm == 0.0: # % solved the equation exactly
                    a = xm
                    b = xm
                    break #% jumps out of the for loop
                    # % decide which half to keep , so that the signs at the ends differ
                if fa * fxm < 0:
                    b = xm
                    fb = fxm
                else:
                    a = xm
                    fa =fxm
                xm = ( a + b )/2
                fxm = f(xm)
                er = abs(b-a)
                i = i+1
            print("i: {:03d} xi: {:+.10f} xm: {:+.10f} xf: {:+.10f} f(xi): {:+.10f} f(xm): {:+.10f} f(xf): {:+.10f} eabs: {:+.10f}\n"
            .format(i, a, fa, xm, fxm, b, fb, er), end="")

            if fxm == 0:
                print (xm,' es raíz.')
                converged = True
            else:
                if er < tol:
                    print (xm,' es aproximación a una raíz con tolerancia ', tol)
                    converged = True
                else:
                    print ('El método fracasó con ', i, ' iteraciones.')
        root = xm
        return [root, i, converged,fa, xm, fxm, fb, er]


def newton(f, df, x0, tol, iter_max):
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
    converged = False

    for i in range(0, iter_max + 1):
        x1 = x0 - (fx/dfx)
        fx= f(x1)
        dfx= df(x1)
        er= math.fabs(x1 - x0)
        x0=x1

        print("i:{:03d} x: {:.10f} fx: {:.10f} error abs: {:.10f} \n"
              .format(i, x0, fx, er ), end="")

        if math.fabs(fx) == 0 or er <= tol or dfx == 0:
            converged = True
            if math.fabs(fx) == 0 :
                print (fx,' es raíz.')
            else:
                if er <= tol:
                    print (x1,' es aproximación a una raíz con tolerancia ', tol)
                else:
                    if dfx == 0:
                        print (x1,' es una posible raíz multiple')
            break
    else:
        print ('El método fracasó con ', i, ' iteraciones.')

    root = fx
    return [root, i, converged]



