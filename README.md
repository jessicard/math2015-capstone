# Math 2015 Capstone

Our capstone calculates the deteminant of a matrix in various ways using Python, and shows the different complexities of each through time tests and graphs.

Group members:
- [Jessica Card](https://github.com/jessicard)
- [Alexander Mies](https://github.com/AlexanderMies)
- [Jacob Million](https://github.com/JacobMMillion)
- Edward Yi


## Running locally
### Dependencies
For graphing, we are using [matplotlib](https://matplotlib.org/). It's recommended to install the dependency on the command line with [pip](https://pypi.org/project/pip/).
```
$ pip install matplotlib
```

### Run an algorithm
To run a specific algorithm, `cd` to this directory in your terminal and run:
```
$ python3 <filename>.py
```

### Git on the Command Line

To pull changes:
```
$ git pull origin main
```

To add all new file changes:
```
$ git add .
```

To add a specific file change:
```
$ git add <filename>
```

To commit your changes:
```
$ git commit -m "Commit message about what you changed"
```

To push your changes to the repo (you may need to pull first):

**NOTE: Please never force push, it's too dangerous when working together!**

```
$ git push origin master
```

## Algorithms
[Computational Complexities of Matrix Multiplication](https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication)

### Laplace Expansion
Time complexity: O(n!)
![Laplace Expansion Graph](/images/laplace_2_electric_boogaloo)

[laplace.py](/laplace.py)

Laplace Expansion, also commonly referred to as the cofactor expansion, method calculates the determinant of a matrix by recursively expanding it along a row or column. In each step, it multiplies the determinant of a smaller submatrix (obtained by removing the current row and column) by the value of the element in the position at which the expansion is taking place. The signs of these products alternate according to the position of the element in the matrix, following a pattern that can be determined by adding the row and column indices of the element (with even sums leading to a positive sign and odd sums to a negative sign). This process continues until the determinant of 2x2 matrices can be directly computed, at which point the recursive expansion concludes.


### Bareiss Algorithm
Time complexity: O(n^3)

![Bareiss Expansion Graph](/images/bareiss_2_the_reckoning.png)

[bareiss.py](/bareiss.py)

During execution of the Bareiss algorithm, every integer that is computed is the determinant of a submatrix of the input matrix. 

The core of the Bareiss algorithm revolves around three nested loops, resulting in an overall complexity of O(n^3). Within these loops, each iteration updates the matrix entries to compute the determinant. However, the crucial logic lies in handling principal minors that become zero during computation. If a principal minor becomes zero, indicating potential singularity, the algorithm must search for a suitable row to swap with the current row. This search ensures the matrix has a non-zero determinant, allowing the algorithm to proceed. If no such row exists for swapping, indicating a singular matrix, the determinant is known to be zero, and the algorithm terminates early. This behavior explains the occasional dips observed in the complexity graph. The algorithm iterates through the matrix, maintaining the previous principal minor (prev) at each step to facilitate computation (as this is the denominator for the following iteration). Below is the core of the Bareiss algorithm (row swapping and other bookeeping code removed for simplicity):

    for i in range(n):
        for j in range(i+1, n):
            for k in range(i+1, n):
                M[j][k] = (M[j][k] * M[i][i] - M[j][i] * M[i][k]) // prev

This algorithm modifies the matrix in place and after calculation, after which the determinant can be found at M[-1][-1], the rightmost entry of the bottom row.


### LU-decomposition
[Wikipedia](https://en.wikipedia.org/wiki/LU_decomposition)
Time complexity: O(n^3)

[lu_decomp.py](/lu_decomp.py)

LU-Decomposition is an algorithm that can be used for solving systems of linear equations, the inversion of matricies, and in our case, computing the determinant of a square matrix. Our goal is given a matrix A, decompose A into three individual components: a lower triangular matrix L, an upper triangular matrix U (not unlike an upper triangular matrix we form with Gaussian elimination), and a permutation matrix P that tracks row swaps -- such that P * A = L * U. In our particular implementation, we initialize square matrix A and a permutation vector P with indices 0-N. The last element of P, (P[N]), counts the number of row swaps to determine the sign of the determinant. For picking the pivots, we iterate through each column [i] and search for the element with the maximum absolute value in that column. In swapping rows, if the row with the maximum element [imax] is not the current row [i], we swap that row with [imax] -- not only swapping within A but modifying the permutation vector P (important for determining sign at the end). After we pivot, we look at all rows below [i] and each element below the specified pivot in the current column is divided by the pivot, forming part of the lower triangular (L) matrix. We then update the remaining elements for each row by subtracting a multiple in the current row (close to Gaussian elimination) to effectively contstruct both the upper and lower triangular matrices in place. Since the determinant of a triangular matrix is the product of it's diagonal elements, and U is the upper triangular after the decomposition, the determinant can be easily calculated once we've decomposed A into LU and determine the sign with P.


## Eigen Decomposition
[Wikipedia](https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix)
Time complexity: O(n^3) (usually)

[eigendecomposition.py](/eigendecomposition.py)

Provided that a matrix is diagonalizable, we can also use a method called Eigen Decomposition to compute the determinant. In this method, we aim to decompose a square matrix A into a product of three matrices: A = PDP^-1 where P is a matrix made up of the eigenvectors of A, and D is a diagonal matrix whose elements are all the eigenvalues of A. The determinant then is the product of its eigenvalues. More simply put, we: 

    1) Compute all eigenvalues of A, which in turn become the diagonal elements of D
    2) Calculate the product of the eigenvalues

Because the determinant of a matrix is equal to the product of its eigenvalues, Eigen Decomposition can be incredibly efficent on smaller matrices, with the exception that the provided matrix is already diagonalizable.

### Strassen
[Wikipedia](https://en.wikipedia.org/wiki/Strassen_algorithm)
Time complexity: O(n^(2.807))


