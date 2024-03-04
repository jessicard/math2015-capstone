import numpy as np
import timeit
import matplotlib
from matplotlib import pyplot as plt

matrix_2 = [
    [1,2],
    [3,4]
]

# Det: 0
matrix_3 = [
    [1,2,3],
    [4,5,6],
    [7,8,10]
]

matrix_5 = [
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5]
]

# RECURSION BABY
def calc_det(matrix):
  # We can just check the outer length because we assume the matrix is square
  # to begin with
  if len(matrix) == 2:
    # Base case, 2x2 matrix
    return ((matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]))

  # Result of the determinant
  sum = 0

  # Any matrix we have here is > 2x2
  for i, x in enumerate(matrix):
    # Chop out 0th column and ith row
    chopped_matrix = []
    for j, _ in enumerate(matrix):
      if i != j:
        chopped_matrix.append(matrix[j][1:])

    for k, _ in enumerate(x):
      if i % 2 == 0:
        if k % 2 == 0:
          sum += x[0] * calc_det(chopped_matrix)
        else:
          sum -= x[0] * calc_det(chopped_matrix)
      else:
        if k % 2 == 0:
          sum -= x[0] * calc_det(chopped_matrix)
        else:
          sum += x[0] * calc_det(chopped_matrix)

  return sum

print(calc_det(matrix_3))

#10000
#~0.004s

#100000
#~.04s

#1000000
#~3.10s

#10000000
#~30.88s


for i in range(1000000):
  runtime = timeit.timeit(lambda: calc_det(matrix_3), number=i)
  print(runtime)
  plt.plot(i, runtime)
