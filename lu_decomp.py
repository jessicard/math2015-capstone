import numpy as np
import timeit
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter


def LUPDecompose(A, Tol=1.0e-9):
    N = len(A)
    P = np.arange(N+1)
    for i in range(N):
        maxA = 0.0
        imax = i
        for k in range(i, N):
            absA = abs(A[k][i])
            if absA > maxA:
                maxA = absA
                imax = k
        if maxA < Tol:
            raise Exception("Matrix is degenerate")
        if imax != i:
            P[i], P[imax] = P[imax], P[i]
            A[[i, imax]] = A[[imax, i]]  # swap rows (allowed?)
            P[N] += 1
        for j in range(i+1, N):
            A[j][i] /= A[i][i]
            A[j][i+1:N] -= A[j][i] * A[i][i+1:N]
    return P

def generate_matrix(N):
    return np.random.rand(N, N)*10

def format_seconds(x, pos):
    return f'{x:.2f} s'

dim = []
runtimes_s = []

for i in range(2, 128):  # can adjust range for sizes
    A = generate_matrix(i)
    start_time = timeit.default_timer()
    P = LUPDecompose(A.copy())  # use A.copy() to avoid modifying the original A
    runtime_s = timeit.default_timer() - start_time  # Directly calculate in seconds
    runtimes_s.append(runtime_s)
    dim.append(i)
    print(f"Matrix size: {i}, Runtime: {runtime_s} s")

plt.plot(dim, runtimes_s, marker='o')
formatter = FuncFormatter(format_seconds)
plt.gca().yaxis.set_major_formatter(formatter)
plt.xlabel('Matrix Size')
plt.ylabel('Runtime (seconds)')
plt.title('LU Decomposition Runtime')
plt.grid(True)
plt.tight_layout()  # Adjust layout
plt.savefig('images/LU_Decomposition_Runtime.png')
#plt.show()  # also show in window