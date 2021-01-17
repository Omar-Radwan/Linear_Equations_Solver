import copy

from methods.matrix_solver import MatrixSolver, print_matrix, multiply


class LuDecomposition(MatrixSolver):
    def __init__(self, matrix: [], result: [], iterations=50):
        super().__init__(matrix, result)
        self.l = [[0 if (i != j) else 1 for j in range(self.SIZE)] for i in range(self.SIZE)]
        self.u = copy.deepcopy(self.matrix)

    def __obtain_zero_and_build_l(self, row: int, col: int, pivot_row: int):
        if self.matrix[row][col] == 0:
            return True
        ratio = self.divide(-self.matrix[row][col], self.matrix[pivot_row][col])
        self.l[row][col] = -ratio
        for cur_col in range(len(self.matrix[row])):
            self.matrix[row][cur_col] += ratio * self.matrix[pivot_row][cur_col]

    def build_lower_zeros_and_build_l(self):
        for row in range(self.SIZE - 1, 0, -1):
            self.__obtain_zero_and_build_l(row, 0, 0)
        for col in range(1, self.SIZE - 1):
            for row in range(self.SIZE - 1, col, -1):
                self.__obtain_zero_and_build_l(row, col, row - 1)

    def propagate_errors(self, matrix_solver):
        self.division_by_zero = matrix_solver.division_by_zero
        self.infinite_solutions = matrix_solver.infinite_solutions
        self.no_solution = matrix_solver.no_solution
        self.not_diagonal_dominant = matrix_solver.not_diagonal_dominant

    def solve(self):
        self.build_lower_zeros_and_build_l()
        l_solver = MatrixSolver(self.l, self.result)
        l_solver.forward_substitution()

        u_solver = MatrixSolver(self.u, l_solver.result)
        u_solver.build_lower_zeros()
        self.result = u_solver.back_substitution()

        if l_solver.has_error:
            self.has_error = l_solver.has_error
            self.error = l_solver.error

        elif u_solver.has_error:
            self.has_error = u_solver.has_error
            self.error = u_solver.error

        return self.result
