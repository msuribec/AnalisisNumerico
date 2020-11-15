import numpy as np

def forward_substitution(L, b):
    y = np.full_like(b, 0)  # Creating the y vector the same size as the b vector
    for k in range(len(b)):
        y[k] = b[k]
        for i in range(k):
            y[k] = y[k] - (L[k, i] * y[i])
        y[k] = y[k] / L[k, k]  # Using forward substitution to find the value of y
    # Returning the y vector
    return y


def backward_substitution(U, y):
    x = np.full_like(y, 0)  # Creating the x vector the same size as the y vector
    for k in range(len(x), 0, -1):
        x[k - 1] = (y[k - 1] - np.dot(U[k - 1, k:], x[k:])) / U[
            k - 1, k - 1]  # Using backward substitution to find the value of x
    # Returning the solution vector x
    return x

# Row oriented forward substitution
def backwardsRows(U,y):

    for i in range(U.shape[0]-1,-1,-1):
        for j in range(i+1, U.shape[1]):
            y[i] -= U[i,j]*y[j]
        y[i] = y[i]/U[i,i]
# Unit row oriented forward substitution
def forwarsRows(L,b):

    for i in range(L.shape[0]):
        for j in range(i):
            b[i] -= L[i,j]*b[j]
    return b


def computing_final_solution(L,U,b):
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x

# converts a row vector to a column vector
def from_vector(vector):
    retval = []
    for r in vector:
        retval.append([r])
    return retval

# given a matrix and a vector, returns the augmented form
def augmentedForm(mat1, mat2):

    retval = []
    for i in range(len(mat1)):
        r = mat1[i]
        newrow = r[:] + mat2[i]
        retval.append(newrow)
    return retval


#row-wise backward substitution
def back(m,n):
    Ab = np.array(m)
    A = Ab[:, 0:n]
    b = Ab[:, n]
    xcomp = np.zeros(n)
    for i in range(n - 1, -1, -1):
        tmp = b[i]
        for j in range(n - 1, i, -1):
            tmp -= xcomp[j] * A[i, j]

        xcomp[i] = tmp / A[i, i]
    return xcomp

# converts matrix and vector to numpy arrays with correct dimensions
def formatVector(mat,coef):
    n=len(mat)
    aux = np.array(mat, dtype=np.double)
    aux1 = np.array(coef, dtype=np.double)
    A = aux.reshape(n, n)
    b = aux1.reshape(n, 1)
    return A,b

def swapCols(arr, start_index, last_index):
    arr[:, [start_index, last_index]] = arr[:, [last_index, start_index]]
    return arr


def swapRows(arr, start_index, last_index):
    arr[[start_index, last_index]] = arr[[last_index, start_index]]
    return arr

