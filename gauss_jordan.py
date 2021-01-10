from gauss_elimination import GaussianElimination
from matrix_solver import MatrixSolver


class GaussJordan(MatrixSolver):
    def __init__(self, matrix: [], result: [], iterations=50):
        super().__init__(matrix, result)

    def solve(self):
        self.build_augmented_matrix()
        self.build_upper_zeros()
        self.build_lower_zeros()
        self.obtain_main_diagonal_ones()
        self.separate_augmented_matrix()
        return self.result
