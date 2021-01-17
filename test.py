from methods.gauss_elimination import GaussianElimination
from methods.gauss_elimination_pivoting import GaussianEliminationPivoting
from methods.gauss_jordan import GaussJordan
from methods.gauss_seidel import GaussSeidel
from methods.lu_decomposition import LuDecomposition
from methods.matrix_solver import MatrixSolver

# matrix = [[1, -1],
#           [5, -5]]
#
# result = [-3, -15]

# matrix = [[1, 1, -1],
#           [6, 2, 2],
#           [-3, 4, 1]]
# result = [-3, 2, 1]

# matrix = [[2, 3, 1],
#           [4, 1, 4],
#           [3, 4, 6]]
# result = [-4, 9, 0]


# matrix = [[12, 3, -5],
#           [1, 5, 3],
#           [3, 7, 13]]
# result = [1, 28, 76]


matrix = [[1, 1, 0, 1],
          [2, 1, -1, 1],
          [4, -1, -2, 2],
          [3, -1, -1, 2]]
result = [2, 1, 0, 3]

gaussian_elimination = GaussianElimination(matrix, result)
gauss_jordan = GaussJordan(matrix, result)
lu_decomposition = LuDecomposition(matrix, result)
gauss_elimination_pivoting = GaussianEliminationPivoting(matrix, result)
gauss_seidel = GaussSeidel(matrix, result, [])

print(f'Gauss Elim: {gaussian_elimination.solve()}')
print(
    f'Gauss Elim Flags: {gaussian_elimination.error}')
print()

print(f'Gauss Jordan: {gauss_jordan.solve()}')
print(
    f'Gauss Jordan Flags: {gauss_jordan.error}')
print()

print(f'LU Decomp: {lu_decomposition.solve()}')
print(
    f'LU Decomp Flags: {lu_decomposition.error}')
print()

print(f'Gauss Elim Piv: {gauss_elimination_pivoting.solve()}')
print(
    f'Gauss Elim Piv Flags: {gauss_elimination_pivoting.error}')
print()

print(f'Gauss Seidel: {gauss_seidel.solve()}')
print(
    f'Gauss Seidal Flags: {gauss_seidel.error}')
print()
