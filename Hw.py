
import numpy as np
#Original Matrix
x = [[1,2],
    [3,4]]


def transpose_matrix(x):
    result = [[0, 0], [0, 0]]
    # Iterate through rows
    for i in range(len(x)):
    #Iterate through columns
        for j in range(len(x[0])):
            result[j][i] = x[i][j]
    for r in result:
        print(r)

transpose_matrix(x)

print(np.transpose(x))
