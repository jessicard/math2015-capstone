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
![Laplace Expansion Graph](/images/laplace.png)

[laplace.py](/laplace.py)

Laplace Expansion, also commonly referred to as the cofactor expansion, method calculates the determinant of a matrix by recursively expanding it along a row or column. In each step, it multiplies the determinant of a smaller submatrix (obtained by removing the current row and column) by the value of the element in the position at which the expansion is taking place. The signs of these products alternate according to the position of the element in the matrix, following a pattern that can be determined by adding the row and column indices of the element (with even sums leading to a positive sign and odd sums to a negative sign). This process continues until the determinant of 2x2 matrices can be directly computed, at which point the recursive expansion concludes.


### Bareiss Algorithm
Time complexity: O(n^3)

![Laplace Expansion Graph](/images/bareiss.png)

[bareiss.py](/bareiss.py)

During execution of the Bareiss algorithm, every integer that is computed is the determinant of a submatrix of the input matrix. 

The core of the Bareiss algorithm revolves around three nested loops, resulting in an overall complexity of O(n^3). Within these loops, each iteration updates the matrix entries to compute the determinant. However, the crucial logic lies in handling principal minors that become zero during computation. If a principal minor becomes zero, indicating potential singularity, the algorithm must search for a suitable row to swap with the current row. This search ensures the matrix remains non-singular, allowing the algorithm to proceed. If no such row exists for swapping, indicating a singular matrix, the determinant is known to be zero, and the algorithm terminates early. This behavior explains the characteristic dips observed in the complexity graph. The algorithm iterates through the matrix, maintaining the previous principal minor (prev) at each step to facilitate computation (as this is the denominator for the following iteration). Below is the core of the Bareiss algorithm (row swapping and other bookeeping code removed for simplicity):

    for i in range(n):
        for j in range(i+1, n):
            for k in range(i+1, n):
                M[j][k] = (M[j][k] * M[i][i] - M[j][i] * M[i][k]) // prev

This algorithm modifies the matrix in place and after calculation, after which the determinant can be found at M[-1][-1], the rightmost entry of the bottom row.


### LU-decomposition
[Wikipedia](https://en.wikipedia.org/wiki/LU_decomposition)
Time complexity: O(n^3)

### Strassen
[Wikipedia](https://en.wikipedia.org/wiki/Strassen_algorithm)
Time complexity: O(n^(2.807))
