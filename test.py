from gauss_elimination import GaussianElimination
from gauss_elimination_pivoting import GaussianEliminationPivoting
from gauss_jordan import GaussJordan
from gauss_seidel import GaussSeidel
from lu_decomposition import LuDecomposition
from matrix_solver import MatrixSolver

"""
10*a+2*b-c-27
-3*a-6*b+2*c+61.5
a+b+5*c+21.5
"""
matrix = [[10, 2, -1],
          [-3, -6, 2],
          [1, 1, 5]]
result = [27, -61.5, -21.5]

# matrix = [[12, 3, -5],
#           [1, 5, 3],
#           [3, 7, 13]]
# result = [1, 28, 76]

# gaussian_elimination = GaussianElimination(matrix, result)
# gauss_jordan = GaussJordan(matrix, result)
# lu_decomposition = LuDecomposition(matrix, result)
# gauss_elimination_pivoting = GaussianEliminationPivoting(matrix, result)
gauss_seidel = GaussSeidel(matrix, result, [])

# print(gaussian_elimination.solve())
# print(gauss_jordan.solve())
# print(lu_decomposition.solve())
# print(gauss_elimination_pivoting.solve())
print(gauss_seidel.solve())

for i in gauss_seidel.iterations_list:
    print(i)
