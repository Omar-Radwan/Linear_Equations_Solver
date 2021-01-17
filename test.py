from gauss_elimination import GaussianElimination
from gauss_elimination_pivoting import GaussianEliminationPivoting
from gauss_jordan import GaussJordan
from gauss_seidel import GaussSeidel
from lu_decomposition import LuDecomposition
from matrix_solver import MatrixSolver

matrix = [[1,-1],
          [5,-5]]

result = [-3,-15]

# matrix = [[12, 3, -5],
#           [1, 5, 3],
#           [3, 7, 13]]
# result = [1, 28, 76]

gaussian_elimination = GaussianElimination(matrix, result)
gauss_jordan = GaussJordan(matrix, result)
lu_decomposition = LuDecomposition(matrix, result)
gauss_elimination_pivoting = GaussianEliminationPivoting(matrix, result)
gauss_seidel = GaussSeidel(matrix, result, [])

print(f'Gauss Elim: {gaussian_elimination.solve()}')
print(f'Gauss Elim Flags: div_by_zero: {gaussian_elimination.division_by_zero}, inf sol: {gaussian_elimination.infinite_solutions}, no sol: {gaussian_elimination.no_solution}')
print(f'Gauss Jordan: {gauss_jordan.solve()}')
print(f'Gauss Jordan Flags: div_by_zero: {gauss_jordan.division_by_zero}, inf sol: {gauss_jordan.infinite_solutions}, no sol: {gauss_jordan.no_solution}')
print(f'LU Decomp: {lu_decomposition.solve()}')
print(f'LU Decomp Flags: div_by_zero: {lu_decomposition.division_by_zero}, inf sol: {lu_decomposition.infinite_solutions}, no sol: {lu_decomposition.no_solution}')
print(f'Gauss Elim Piv: {gauss_elimination_pivoting.solve()}')
print(f'Gauss Elim Piv Flags: div_by_zero: {gauss_elimination_pivoting.division_by_zero}, inf sol: {gauss_elimination_pivoting.infinite_solutions}, no sol: {gauss_elimination_pivoting.no_solution}')
print(f'Gauss Seidel: {gauss_seidel.solve()}')
print(f'Gauss Sedal Flags: div_by_zero: {gauss_seidel.division_by_zero}, inf sol: {gauss_seidel.infinite_solutions}, no sol: {gauss_seidel.no_solution}')
for i in gauss_seidel.iterations_list:
    print(i)
