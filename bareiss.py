# Bareiss Algorithm

# Citation:
# Wikipedia: https://en.wikipedia.org/wiki/Bareiss_algorithm#:~:text=In%20mathematics%2C%20the%20Bareiss%20algorithm,(there%20is%20no%20remainder).
# Stack Overflow: https://stackoverflow.com/questions/66192894/precise-determinant-of-integer-nxn-matrix

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


def bareiss_algorithm(M):

    N = len(M)
    sign = 1
    prev = 1

    # begining actual algo
    for i in range(N-1):

        # if principal minors == 0, need to swap rows
        if M[i][i] == 0:  # swap with another row having nonzero i's elem
            # finding a row to swap
            swapto = next((j for j in range(i+1, N) if M[j][i] != 0), None)
            if swapto is None:
                return 0  # all M[*][i] are zero => zero determinant

            # swapping the rows, and flipping the sign
            M[i] = M[swapto]
            M[swapto] = M[i]
            sign = -sign

        # now we are working with an approproate row with non-zero principle minor
        for j in range(i+1, N):
            for k in range(i+1, N):

                # applying the formula
                M[j][k] = (M[j][k] * M[i][i] - M[j][i] * M[i][k]) // prev

        prev = M[i][i]  # updating for next iteration

    # done, returning determinant
    # print(sign * M[-1][-1])
    return sign * M[-1][-1]


dim = []
runtimes = []

# This is O(n^3)
for i in range(2, 200):
    mx = generate_matrix(i)
    # print(mx)

    runtime = timeit.timeit(lambda: bareiss_algorithm(mx), number=1)
    runtimes.append(runtime)
    dim.append(i)
    # print(runtime)

plt.plot(dim, runtimes)
plt.show()
