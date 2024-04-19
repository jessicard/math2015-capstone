# Math 2015 Capstone

Our capstone calculates the deteminant of a matrix in various ways using Python, and shows the different complexities of each through time tests and graphs.

Group members:
- [Jessica Card](https://github.com/jessicard)
- [Alexander Mies](https://github.com/AlexanderMies)
- [Jacob Million](https://github.com/JacobMMillion)
- [Edward Yi](https://github.com/Edward-D-Yi)


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
[Wikipedia](https://en.wikipedia.org/wiki/Laplace_expansion)
Time complexity: O(n!)

![Laplace Expansion Graph](/images/laplace_2_electric_boogaloo.png)

[laplace.py](/laplace.py)

Laplace Expansion, also commonly referred to as the cofactor expansion, method calculates the determinant of a matrix by recursively expanding it along a row or column. In each step, it multiplies the determinant of a smaller submatrix (obtained by removing the current row and column) by the value of the element in the position at which the expansion is taking place. The signs of these products alternate according to the position of the element in the matrix, following a pattern that can be determined by adding the row and column indices of the element (with even sums leading to a positive sign and odd sums to a negative sign). This process continues until the determinant of 2x2 matrices can be directly computed, at which point the recursive expansion concludes.


### Bareiss Algorithm
Time complexity: O(n^3)

![Bareiss Expansion Graph](/images/bareiss_2_the_reckoning.png)

[bareiss.py](/bareiss.py)

The Bareiss algorithm can be thought of as a “Multistep Integer-Preserving Gaussian Elimination” as was the paper titled by Erwin H. Bareiss, the mathematician that developed the algorithm. This algorithm can be applied to matrices with integer entries. It is unique as it uses only integer arithmetic in its procedure, and the division performed in the code below is guaranteed to result in an integer without remainder. In code, this looks three nested ‘for’ loops which modify the matrix in place.

The procedure is as follows: Begin at the top left-most entry. This is M[i,i] for i=0. Then, for j,k=i+1, begining at the entry one to the right of i and one entry down, the formula: M[j][k] = (M[j][k] * M[i][i] - M[j][i] * M[i][k]) / prev, is applied. The variable prev is originally initiated to 1 and represents the previous M[i][i]. After iterating over all k for the second row and applying the formula, the next row is then iterated over and this repeats until the bottom right-most entry is modified. At this point, i is incremented, M[i][i] is set to be the current M[i][i], and the process repeats for i=2: i[2][2], the next diagonal entry. This repeats until i reaches the second to last row and the final iteration is ran. The determinant is then found at the bottom right-most entry or M[-1][-1], as the matrix is modified in place.

Like in Gaussian elimination, rows can be swapped in this procedure if necessary. If any A[i,i] becomes zero during computation, or is 0, a suitable row to swap with is searched for and swapped with if one exists. If this is done, the sign of the determinant is flipped in correspondance with each swap. Otherwise, the determinant is zero and the algorithm terminates early. The algorithm used in the code for this project functions only for an n x n matrix. Below is the core of the Bareiss algorithm, implemented in Python (row swapping and other bookeeping code removed for simplicity):

    # Simplified Bareiss Algorithm:
    
    for i in range(N-1): # where N is the size of the matrix

        # ensure non-zero M[i][i]
        # flip sign if zero M[i][i] and suitable swap row exists, swap
        # return 0 if zero M[i][i] and suitable swap row does not exist

        for j in range(i+1, N):
            for k in range(i+1, N):

                # applying the formula
                M[j][k] = (M[j][k] * M[i][i] - M[j][i] * M[i][k]) // prev

        prev = M[i][i]  # updating for next iteration

    # returning the determinant, located at the bottom rightmost position
    return sign * M[-1][-1]



### LU-decomposition
[Wikipedia](https://en.wikipedia.org/wiki/LU_decomposition)
Time complexity: O(n^3)

![LU-Decomposition Graph](/images/LU_Decomposition_Runtime.png)

[lu_decomp.py](/lu_decomp.py)

LU-Decomposition is an algorithm that can be used for solving systems of linear equations, the inversion of matricies, and in our case, computing the determinant of a square matrix. Our goal is given a matrix A, decompose A into three individual components: a lower triangular matrix L, an upper triangular matrix U (not unlike an upper triangular matrix we form with Gaussian elimination), and a permutation matrix P that tracks row swaps -- such that P * A = L * U. In our particular implementation, we initialize square matrix A and a permutation vector P with indices 0-N. The last element of P, (P[N]), counts the number of row swaps to determine the sign of the determinant. For picking the pivots, we iterate through each column [i] and search for the element with the maximum absolute value in that column. In swapping rows, if the row with the maximum element [imax] is not the current row [i], we swap that row with [imax] -- not only swapping within A but modifying the permutation vector P (important for determining sign at the end). After we pivot, we look at all rows below [i] and each element below the specified pivot in the current column is divided by the pivot, forming part of the lower triangular (L) matrix. We then update the remaining elements for each row by subtracting a multiple in the current row (close to Gaussian elimination) to effectively contstruct both the upper and lower triangular matrices in place. Since the determinant of a triangular matrix is the product of it's diagonal elements, and U is the upper triangular after the decomposition, the determinant can be easily calculated once we've decomposed A into LU and determine the sign with P.


Because we require n additions and n multiplications in the first column of an nxn matrix, the first column can be expressed as 2n(n-1). The second column then requires n-1 additions and n-1 multiplications, yielding 2(n - 1)(n - 2). Doing this for n number of rows yields the sum of 2(n-i)(n-i+1) for i=1 to n. This can be expressed as 2/3 n^3, and dropping the constant gives us an in practice time complexity of O(n^3). 


## Eigen Decomposition
[Wikipedia](https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix)
Time complexity: O(n^3) (usually)

![Eigenvalue Decomposition Graph](/images/eigendecomposition.png)

[eigendecomposition.py](/eigendecomposition.py)

Provided that a matrix is diagonalizable, we can also use a method called Eigen Decomposition to compute the determinant. In this method, we aim to decompose a square matrix A into a product of three matrices: A = PDP^-1 where P is a matrix made up of the eigenvectors of A, and D is a diagonal matrix whose elements are all the eigenvalues of A. The determinant then is the product of its eigenvalues. More simply put, we: 

    1) Compute all eigenvalues of A, which in turn become the diagonal elements of D
    2) Calculate the product of the eigenvalues

Because the determinant of a matrix is equal to the product of its eigenvalues, Eigen Decomposition can be incredibly efficent on smaller matrices, with the exception that the provided matrix is already diagonalizable.

Although in theory Eigen Decomposition can be as fast as matrix multiplication (which can be done with O(nw) arithmatic operations), the operations are instead over polynomials of degree n and, as a result, bump the runtime up to O(n^3) in practice. [Victor Y. Pan, Zhao Q. Chen: The Complexity of the Matrix Eigenproblem. STOC 1999: 507-516] This operation can be done quite efficiently for smaller matrices, but as we increase in size the likelihood of having to do more computationally complex operations involving complex numbers and roots increases, hence the O(n^3) time complexity observed in practice.

### Strassen
[Wikipedia](https://en.wikipedia.org/wiki/Strassen_algorithm)
Time complexity: O(n^(2.807))


