
from sympy.parsing.sympy_parser import parse_expr
import sympy as sp
import oneVariableEquations.bisection as bisection
import oneVariableEquations.busquedasInc as incsearch
import oneVariableEquations.newton as newton
import oneVariableEquations.ptofijo as fixedpoint
import oneVariableEquations.raicesmult as multroots
import oneVariableEquations.reglaFalsa as regfalsi
import oneVariableEquations.secant as secant


import integration.Integration as integration

import linearSystems.directMethods.cholesky as cholesky
import linearSystems.directMethods.crout as crout
import linearSystems.directMethods.Doolittle as doolittle
import linearSystems.directMethods.GaussSimple as gsimple

import linearSystems.directMethods.GaussPartial as gpartial
import linearSystems.directMethods.gaussTotalPivot as gtotal
import linearSystems.directMethods.LUGaussPartial as lupartial
import linearSystems.directMethods.LUGaussSimple as lusimple


import linearSystems.iterativeMethods.jacobi as jacobi
import linearSystems.iterativeMethods.gaussSeidel as gseidel

import interpolation.vandermonde as vandermonde
import interpolation.difDiv as difdiv
import interpolation.lagrange as lagrange
import interpolation.linearSpline as lspline
import interpolation.quadraticSplines as qsplines
import interpolation.cubicSplines as csplines
class CustomError(object):
    pass


def getMatrixInput(n):
    matrix=[]

    for i in range(n):
       print('Please enter row %d, separating numbers with a comma'%(i+1))

       # taking row input from the user
       row = list(map(float, input().split(',')))
       # appending the 'row' to the 'matrix'
       matrix.append(row)

    isSquare(matrix)
    if isSquare(matrix):
        return matrix
    else:
       print("Please enter a square matrix")
       return getMatrixInput(n)



def isSquare (m):
    return all (len (row) == len (m) for row in m)


def getVectorInput(n):

    row = list(map(float, input().split(',')))
    return row

def getSystemInput():
    try:
        n=int(input("Enter the number of columns and rows of your matrix:"))
    except ValueError:
        print("This is not a whole number.")
    A=getMatrixInput(n)
    print('please enter the vector of independent terms for the system, each number must be separated by a comma')
    b=getVectorInput(n)
    if n==len(b):
        return A,b
    else:
       print("The vector of independent must have n numbers to solve and nxn system of equations")
       return getSystemInput()


def getItSystemInput():
    try:
        n=int(input("Enter the number of columns and rows of your matrix:"))
    except ValueError:
        print("This is not a whole number.")
    A=getMatrixInput(n)
    print('please enter the vector of independent terms for the system, each number must be separated by a comma')
    b=getVectorInput(n)
    print('please enter the initial solution vector')
    x = getVectorInput(n)
    if n==len(b) & len(b)==len(x):
        return A,b,x
    else:
       print("n must be the same for the vector of independent terms , the initial solution vector and the matrix ")
       return getSystemInput()


def getInterpolationSystem():
    try:
        n=int(input("Enter the number of points to be used"))
    except ValueError:
        print("This is not a whole number.")
    print('Enter the x vector')
    x = getVectorInput(n)
    print('Enter the f(x) vector')
    y = getVectorInput(n)
    if len(x)==len(y):
        return x,y
    else:
       print("Both vectors must have equal number of elements")
       return getInterpolationSystem()

#obtain nummpy function for integration
def getNumpyFunction():
    x = sp.Symbol('x')
    str=input("Enter the function :")
    expr=parse_expr(str, evaluate=False)
    f = sp.lambdify(x, expr, "numpy")
    return f


#obtain sympy function for solving equations of one variable
def getSympyFunction():
    x = sp.Symbol('x')
    str=input("Enter the function f:")
    expr=parse_expr(str, evaluate=False)
    return expr

def getSympyFunctionG():
    x = sp.Symbol('x')
    str=input("Enter the function g:")
    expr=parse_expr(str, evaluate=False)
    return expr

def getFloatInput(msg=''):
    return float( input(msg))

def getIntInput(msg=''):
    return int(input(msg))

def startIntegration(k):
    if k==1:#trapz method
        f=getNumpyFunction()
        a=getFloatInput('Enter a:')
        print('Enter b:')
        b=getFloatInput()
        integration.trapz(f,a,b)
    elif k==2:#composite trapz method
        f = getNumpyFunction()
        print('Enter a:')
        a = getFloatInput()
        print('Enter b:')
        b = getFloatInput()
        print('Enter the number of trapezoids:')
        N=getIntInput()
        integration.trapzComp(f,a,b,N)
    elif k==3:# simpson 1/3 method
        f = getNumpyFunction()
        print('Enter a:')
        a = getFloatInput()
        print('Enter b:')
        b = getFloatInput()
        integration.simps(f,a,b)
    elif k==4:#simpson 1/3 generalized
        f = getNumpyFunction()
        print('Enter a:')
        a = getFloatInput()
        print('Enter b:')
        b = getFloatInput()
        print('Enter the number of trapezoids:')
        N = getIntInput()
        integration.simpsComp(f,a,b,N)
    elif k==5:#simpson 3/8
        f = getNumpyFunction()
        print('Enter a:')
        a = getFloatInput()
        print('Enter b:')
        b = getFloatInput()
        integration.simpson38(f,a,b)
    else:
        print('That is not an accepted number')




def startDirectSystem(k):
    A,b=getSystemInput()
    if k == 1:  # Gauss Simple
        gsimple.solveGaussSimple(A,b)
    elif k == 2:  # Gauss Partial pivot
        gpartial.solveGaussPartial(A,b)
    elif k == 3:  # Gauss total pivot
        gtotal.solveGaussT(A,b)
    elif k == 4:  # LU fact
        lusimple.solveLUSimple(A,b)
    elif k == 5:  # LU fact with partial pivot
        lupartial.solveLUGaussPartial(A,b)
    elif k == 6: #cholesky
        cholesky.solveChol(A,b)
    elif k == 7: #crout
        crout.solveCrout(A,b)
    elif k==8: # doolittle
        doolittle.solveDoolittle(A,b)
    else:
        print('That is not an accepted number')


def startIterativeSystem(k):
    A,b,x =getItSystemInput()
    tol=getFloatInput()
    nmax= getItSystemInput()
    if k == 1:  # Jacobi
        jacobi.jacobi(A,b,x,tol,nmax)
    elif k == 2:  # Gauss Seidel
        gseidel.gausSeidel(A,b,x,tol,nmax)
    else:
        print('That is not an accepted number')

def startOneVarEqs(k):
    if k == 1:  # inc search
        x = sp.Symbol('x')
        f = getSympyFunction()
        print('Enter x0:')
        x0 = getFloatInput()
        print('Enter the tolerance:')
        tol=getFloatInput()
        print('Enter the number of max iterations:')
        iter_max=getIntInput()
        incsearch.busquedasIncrementales(x,f,x0,tol,iter_max)
    elif k == 2: # bisection
        x = sp.Symbol('x')
        f = getSympyFunction()
        print('Enter a:')
        a = getFloatInput()
        print('Enter b:')
        b = getFloatInput()
        print('Enter the tolerance:')
        tol=getFloatInput()
        print('Enter the number of max iterations:')
        iter_max=getIntInput()
        bisection.bisection(x, f, a, b, tol, iter_max)
    elif k == 3:  # regula falsi
        x = sp.Symbol('x')
        f = getSympyFunction()
        print('Enter a:')
        a = getFloatInput()
        print('Enter b:')
        b = getFloatInput()
        print('Enter the tolerance:')
        tol=getFloatInput()
        print('Enter the number of max iterations:')
        iter_max=getIntInput()
        regfalsi.reglaFalsa(x,f,a,b,tol,iter_max)
    elif k == 4:  # fixed point
        x = sp.Symbol('x')
        f = getSympyFunction()
        g = getSympyFunctionG()
        print('Enter x0:')
        x0=getFloatInput()
        print('Enter the tolerance:')
        tol = getFloatInput()
        print('Enter the number of max iterations:')
        iter_max = getIntInput()
        fixedpoint.puntofijo(x,f,g,x0,iter_max,tol)
    elif k == 5:  # newton
        x = sp.Symbol('x')
        f = getSympyFunction()
        print('Enter x0:')
        x0 = getFloatInput()
        print('Enter the tolerance:')
        tol = getFloatInput()
        print('Enter the number of max iterations:')
        iter_max = getIntInput()
        newton.newton(x, f, x0, tol, iter_max)
    elif k==6: # secant
        f = getSympyFunction()
        print('Enter x0:')
        x0 = getFloatInput()
        print('Enter x1:')
        x1 = getFloatInput()
        print('Enter the tolerance:')
        tol = getFloatInput()
        print('Enter the number of max iterations:')
        iter_max = getIntInput()
        secant.secant(x,f,x0,x1,iter_max,tol)
    elif k==7: # mult roots
        x = sp.Symbol('x')
        f = getSympyFunction()
        print('Enter x0:')
        x0 = getFloatInput()
        print('Enter the tolerance:')
        tol = getFloatInput()
        print('Enter the number of max iterations:')
        iter_max = getIntInput()
        multroots.rmult(x,f,x0,iter_max,tol)
    else:
        print('That is not an accepted number')

def startInterpolation(k):
    x,y=getInterpolationSystem()
    if k == 1:  # vandermonde
       vandermonde.vanderMonde(x,y)
    elif k == 2:  # dif div
        difdiv.interpolate_newton(x,y)
    elif k == 3:  # lagrange
        lagrange.lagrange_pol(x,y)
    elif k == 4:  # linear Spline
        lspline.linearSplines(x,y)
    elif k == 5:  # quadratic Splines
        qsplines.solvequadsplines(x,y)
    elif k == 6: # cubic splines
        csplines.cubicSpline(x,y)
    else:
        print('That is not an accepted number')


def startInput():
    print(
        '''
        Choose the type of method you want to run:
        1 -- Integration methods
        2 -- Interpolation methods
        3 -- Systems of equations (direct methods)
        4 -- Systems of equations (iterative methods)
        5 -- One variable equations
        '''
    )
    ind=getIntInput('Choose a number')

    if ind==1:#integration
        print(
            '''
            Choose the integration method you want to run:
            1 -- Trapezoid method
            2 -- Generalized trapezoid method
            3 -- Simpson 1/3 method
            4 -- Simpson 1/3 generalized method
            5 -- Simpson 3/8 method
            '''
        )
        ind2 = getIntInput()
        startIntegration(ind2)

    elif ind==2: #interpolation
        print(
            '''
            Choose the interpolation method you want to run:
            1 -- Vandermonde
            2 -- Divided differences (Newton's polynomial)
            3 -- Lagrange
            4 -- Linear Splines
            5 -- Quadratic splines
            6 -- Cubic splines
            '''
        )
        ind2 = getIntInput()
        startInterpolation(ind2)
    elif ind==3: # direct systems
        print(
            '''
            Choose the direct method you want to run:
            1 -- Gaussian elimination
            2 -- Gaussian elimination with partial pivoting
            3 -- Gaussian elimination with total pivoting
            4 -- LU factorization with Gaussian elimination (no pivoting)
            5 -- LU factorization with Gaussian elimination and partial pivoting
            6 -- Cholesky
            7 -- Crout
            8 -- Doolittle
            '''
        )
        ind2 = getIntInput()
        startDirectSystem(ind2)
    elif ind == 4: #iterative systems
        print(
            '''
            Choose the iterative method you want to run:
            1 -- Jacobi
            2 -- Gauss Seidel
            '''
        )
        ind2 = getIntInput()
        startIterativeSystem(ind2)
    elif ind == 5: #one var equations
        print(
            '''
            Choose the method you want to run:
            1 -- Incremental search
            2 -- Bisection
            3 -- Regula falsi
            4 -- Fixed point
            5 -- Newton
            6 -- Secant
            7 -- Multiple roots
            '''
        )
        ind2 = getIntInput()
        startOneVarEqs(ind)
    else:
        print('That is not an expected input')



if __name__ == '__main__':
    startInput()


