from misc.constants import GAUSS_JORDAN
from methods.matrix_solver import MatrixSolver


class GaussJordan(MatrixSolver):
    def __init__(self, matrix: [], result: [], iterations=50):
        super().__init__(matrix, result)
        self.name = GAUSS_JORDAN

    def solve(self):
        self.build_augmented_matrix()
        self.build_lower_zeros()
        self.build_upper_zeros()
        self.obtain_ones_in_the_main_diagonal()
        self.separate_augmented_matrix()
        return self.result
