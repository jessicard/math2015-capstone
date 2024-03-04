import timeit
import random
from matplotlib import pyplot as plt

def generate_matrix(sz):
  matrix = []
  for i in range(sz):
    matrix.append([])
    for j in range(sz):
      matrix[i].append(random.randint(0,9))

  return matrix

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

    # We have to alternate + / - for this algorithm
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

dim = []
runtimes = []

# This is O(n!), if you increase this upper bound, prepare to wait... forever
for i in range(2, 9):
  mx = generate_matrix(i)
  print(mx)

  runtime = timeit.timeit(lambda: calc_det(mx), number=1)
  runtimes.append(runtime)
  dim.append(i)
  print(runtime)

plt.plot(dim, runtimes)
plt.show()
