import math

xin = input("xin ")
xs = input("xs ")
tolerancia = input("tolerancia ")
iteraciones = input("iteraciones ")

def reglaFalsa(xin,xs,tolerancia,iteraciones):
    fxin = f(xin)
    fxs = f(xs)
    if fxin == 0:
        print(str(xin) + " Es raiz")
    elif fxs == 0:
        print(str(xs) + " Es raiz")
    elif (fxin * fxs < 0 ):
        xmedio = xin - ((fxin * (xs-xin))/(fxs -fxin))
        n = 1
        fxmedio = f(xmedio)
        err = tolerancia +1
        #print('iter | xin | xmedio  | fx  |  err')
        print('{:30} {:30} {:30} {:30} {:30}'.format('iter', 'xin', 'xmedio', 'fx', 'err'))
        #print(n - 1 , "|", xin, "|", xmedio, "|", fxmedio , "|", err )
        print('{:30} {:30} {:30} {:30} {:30}'.format(str(n - 1), str(xin), str(xmedio), str(fxmedio), str(err)))
        while(err > tolerancia ) and (fxmedio != 0) and (n < iteraciones):
            if fxin * fxmedio <0:
                xs = xmedio
                fxs = fxmedio
            else:
                xin = xmedio
                fxin = fxmedio
            temp = xmedio
            xmedio = xin - ((fxin * (xs-xin))/(fxs -fxin))
            fxmedio = f(xmedio)
            err = abs(xmedio - temp)
            n = n + 1
            #print(n, "|", xin, "|", xmedio, "|", fxmedio , "|", err )
            print('{:30} {:30} {:30} {:30} {:30}'.format(str(n), str(xin), str(xmedio), str(fxmedio), str(err)))
        if fxmedio == 0:
            print(str(xmedio) + " es raiz ")
        elif err< tolerancia:
            print(str(xmedio) + " es una raiz aproximada con tolerancia de = " + str(tolerancia) )
        else:
            print("Fallo con" + str(iteraciones) + " iteraciones.")
    else:
        print("Intervalo inadecuado.")

def f(x):
    return math.exp(-x+1) - x**2 + 4*x + 7*(math.cos(x**2 - 4)**2) - 7
    #return math.exp(-(x*x) + 1) - 4*x*x*x +25

def main():
    reglaFalsa(xin, xs, tolerancia, iteraciones)

if __name__ == '__main__':
    main()