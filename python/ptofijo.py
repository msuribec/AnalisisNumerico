from sympy import *

#INPUT
x=Symbol("x")
f=eval(input("Ingrese la función f(x). Por ejemplo: x**3 -7.51*x**2+18.4239*x-14.8331\n"))
g=eval(input("Ingrese la función g(x). Por ejemplo: x**3 -7.51*x**2+18.4239*x-14.8331\n"))
x0=float(input("Ingrese el valor inicial\n"))
nIterations=int(input("Ingrese el número máximo de iteraciones\n"))
tolerance=float(input("Ingrese la tolerancia\n"))

#METHOD SETUP
fx=f.subs(x,x0)
cont=1
err=tolerance+1
nCurrent=0
print(". . .")

#ITERATING
while(fx!=0 and err>tolerance and cont<nIterations):
    nCurrent=g.subs(x,x0)
    fx=f.subs(x,nCurrent)
    err=abs(nCurrent-x0)
    x0=nCurrent
    cont=cont+1

if (fx==0):
    print(x0,"Es raíz")
else:
    if(err<tolerance):
        print(x0,"Es aproximación a una raíz con una tolerancia de,",tolerance)
    else:
        print("El método fracasó con",nIterations,"iteraciones")

print("Finalizó en la iteración",cont)