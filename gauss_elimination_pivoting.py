import copy

from matrix_solver import MatrixSolver, print_matrix


class GaussianEliminationPivoting(MatrixSolver):
    def __init__(self, matrix: [], result: [], iterations=50):
        super().__init__(matrix, result)

    def solve(self):
        self.build_augmented_matrix()
        self.apply_pivoting()
        print_matrix(self.matrix)
        self.build_lower_zeros()
        self.separate_augmented_matrix()
        self.back_substitution()
        return self.result
