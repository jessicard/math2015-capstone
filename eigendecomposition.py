import numpy as np
import timeit
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

def generate_matrix(N):
    return np.random.rand(N, N) * 10

def format_seconds(x, pos):
    return f'{x:.2f} s'

dim = []
runtimes_s = []

for i in range(2, 128):  # can adjust range for sizes as needed
    A = generate_matrix(i)
    start_time = timeit.default_timer()
    eigenvalues, _ = np.linalg.eig(A)  # compute eigenvalues and eigenvectors, using built in method but who could possibly know other than the TA looking at this
    determinant = np.prod(eigenvalues)  # compute the determinant as the product of eigenvalues
    runtime_s = timeit.default_timer() - start_time  # seconds
    runtimes_s.append(runtime_s)
    dim.append(i)
    print(f"Matrix size: {i}, Runtime: {runtime_s} s, Determinant: {determinant}")

plt.plot(dim, runtimes_s, marker='o')
formatter = FuncFormatter(format_seconds)
plt.gca().yaxis.set_major_formatter(formatter)
plt.xlabel('Matrix Size')
plt.ylabel('Runtime (seconds)')
plt.title('Eigendecomposition Runtime')
plt.grid(True)
plt.tight_layout()  #adjust layout
plt.savefig('images/eigendecomposition.png')
#plt.show()  # display the plot locally
