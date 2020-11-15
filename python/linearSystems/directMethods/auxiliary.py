import numpy as np
#
# def transpose(mat):
#     """
# 	Return a transposed version of mat.
# 	"""
#     retval = []
#     for c in range(len(mat[0])):
#         newrow = []
#         for r in range(len(mat)):
#             newrow.append(mat[r][c])
#         retval.append(newrow)
#     return retval
#
#
# def row_swap_mat(i, j):
#     P = np.eye(n)
#     P[i] = 0
#     P[j] = 0
#     P[i, j] = 1
#     P[j, i] = 1
#     return P
#

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


def backwardsRows(U,y):
    """ Row oriented backward substitution """
    for i in range(U.shape[0]-1,-1,-1):
        for j in range(i+1, U.shape[1]):
            y[i] -= U[i,j]*y[j]
        y[i] = y[i]/U[i,i]
    return y

def forwarsRows(L,b):
    """ Unit row oriented forward substitution """
    for i in range(L.shape[0]):
        for j in range(i):
            b[i] -= L[i,j]*b[j]
    return b


def computing_final_solution(L,U,b):
    # Creating the L and U matrices using the specified algorithm

    # Calling forward then backward substitution

    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    # Returning the solution vector x
    return x

def from_vector(vector):
    """
	Convert a vector into a column matrix.
	"""
    retval = []
    for r in vector:
        retval.append([r])
    return retval


def augmentedForm(mat1, mat2):
    """
	Duct-tape mat2's columns to the right of mat1
	Return a new matrix.
	"""
    retval = []
    for i in range(len(mat1)):
        r = mat1[i]
        newrow = r[:] + mat2[i]
        retval.append(newrow)
    return retval

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

