# Bareiss Algorithm

# May or may not need to be modified to account for scaling...

import timeit
import random
from matplotlib import pyplot as plt


def generate_matrix(sz):
    matrix = []
    for i in range(sz):
        matrix.append([])
        for j in range(sz):
            matrix[i].append(random.randint(0, 9))

    return matrix


def bareiss_algorithm(matrix):
    n = len(matrix)

    # Assuming leading principal minors are all non-zero
    # Matrix is modified in-place
    for k in range(1, n):
        for i in range(k, n):
            for j in range(k, n):
                matrix[i][j] = (matrix[i][j] * matrix[k-1][k-1] -
                                matrix[i][k-1] * matrix[k-1][j]) / matrix[k-1][k-1]

    # Compute the determinant, simply the n,n of the matrix
    determinant = matrix[n-1][n-1]
    return determinant


dim = []
runtimes = []

# This is O(n^3), if you increase this upper bound, prepare to wait... forever
for i in range(2, 8):
    mx = generate_matrix(i)
    print(mx)

    runtime = timeit.timeit(lambda: bareiss_algorithm(mx), number=1)
    runtimes.append(runtime)
    dim.append(i)
    print(runtime)

plt.plot(dim, runtimes)
plt.show()
