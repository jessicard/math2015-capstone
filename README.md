# Math 2015 Capstone

Our capstone calculates the deteminant of a matrix in various ways, and shows the different complexities of each through timing and graphs.

[Computational Complexities of Matrix Multiplication](https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication)

## Laplace Expansion
Time complexity: O(n!)

[laplace.py](/laplace.py)

Laplace Expansion, also commonly referred to as the cofactor expansion, method calculates the determinant of a matrix by recursively expanding it along a row or column. In each step, it multiplies the determinant of a smaller submatrix (obtained by removing the current row and column) by the value of the element in the position at which the expansion is taking place. The signs of these products alternate according to the position of the element in the matrix, following a pattern that can be determined by adding the row and column indices of the element (with even sums leading to a positive sign and odd sums to a negative sign). This process continues until the determinant of 2x2 matrices can be directly computed, at which point the recursive expansion concludes.

TODO: Add more algorithms!
Some other examples of algorithms:

## Bareiss Algorithm
[Wikipedia](https://en.wikipedia.org/wiki/Bareiss_algorithm)
Time complexity: O(n^3)

## LU-decomposition
[Wikipedia](https://en.wikipedia.org/wiki/LU_decomposition)
Time complexity: O(n^3)

## Strassen
[Wikipedia](https://en.wikipedia.org/wiki/Strassen_algorithm)
Time complexity: O(n(2.807))