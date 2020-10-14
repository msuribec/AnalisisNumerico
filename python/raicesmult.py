from sympy import *

#INPUT
x=Symbol("x")
f=eval(input("Ingrese la función f(x). Por ejemplo: exp(-x)-x\n"))
x0=float(input("Ingrese el valor inicial\n"))
nIterations=int(input("Ingrese el número máximo de iteraciones\n"))
tolerance=float(input("Ingrese la tolerancia\n"))

#METHOD SETUP
fx=f.subs(x, x0)            #f(x0) [Evaluating]
fp=f.diff(x)                #f'(x)
fpx=fp.subs(x,x0)           #f'(x0) [Evaluating]
fpp=fp.diff(x)              #f''(x)
fppx=fpp.subs(x,x0)         #f''(x0) [Evaluating]
cont=1
# print(f)
# print(fx)
# print(fp)
# print (fpx)
# print(fpp)
# print(fppx)
denominator=(fpx**2)-(fx*fppx)
err=tolerance+1
nCurrent=0
print(". . .")

#ITERATING
while(denominator!=0 and fx!=0 and err>tolerance and cont<nIterations):
    x1=x0-(fx*fpx)/denominator
    fx=f.subs(x,x1)
    fpx=fp.subs(x,x1)
    fppx=fpp.subs(x,x1)
    denominator=(fpx**2)-(fx*fppx)
    err=abs(x1-x0)
    x0=x1
    cont=cont+1

#RESULT
if(fx==0):
    print(x0, "Es una raíz")
else:
    if(err<tolerance):
        print(x1, "Es aproximación a una raíz con tolerancia de", tolerance)
    else:
        if(denominator==0):
            print("Se encontró una división por 0")
        else:
            print("El método fracasó brutalmente con", nIterations,"iteraciones")

print("Finalizó en la iteración",cont)