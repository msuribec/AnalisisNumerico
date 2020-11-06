
import numpy as np

def doolittle():
    #Hard-coded A matrix values
    matrizA = np.array([[1,2],[3,4]])
    matrizU = np.zeros(matrizA.shape)
    matrizL = np.zeros(matrizA.shape)

    print("____________Matriz A_______________")
    print(matrizA)
    print("___________________________________")

    tmpMatriz = matrizA.shape[0]

    for j in range(tmpMatriz):
        matrizL[j][j] = 1.0
        for i in range(j + 1):
            tmp = sum(matrizU[k][j] * matrizL[i][k] for k in range(i))
            matrizU[i][j] = matrizA[i][j] - tmp
        for i in range(j, tmpMatriz):
            tmp1 = sum(matrizU[k][j] * matrizL[i][k] for k in range(j))
            matrizL[i][j] = (matrizA[i][j] - tmp1) / matrizU[j][j]

    print("____________Matriz L_______________")
    print(matrizL)
    print("___________________________________")

    print("____________Matriz U_______________")
    print(matrizU)
    print("___________________________________")


def main():
    doolittle()

if __name__ == '__main__':
    main()