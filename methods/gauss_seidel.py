import copy

from misc.gauss_seidel_iteration import GaussSeidelIteration
from methods.matrix_solver import MatrixSolver, GAUSS_SEIDEL


class GaussSeidel(MatrixSolver):
    def __init__(self, matrix: [], result: [], initials, iterations=50, precision=0.00001):
        super().__init__(matrix, result)
        self.iterations = iterations
        self.iterations_list = []
        self.prev_solution = []
        if len(initials) == 0:
            self.solution = [0 for i in range(self.SIZE)]
        else:
            self.solution = copy.deepcopy(initials)
        self.prev_solution = copy.deepcopy(self.solution)
        self.precision = precision
        self.name = GAUSS_SEIDEL

    def do_iteration(self):
        for row in range(self.SIZE):
            cur_solution = self.result[row]
            for col in range(self.SIZE):
                if row != col:
                    cur_solution -= (self.solution[col] * self.matrix[row][col])
            self.check_solvability(self.matrix[row][row], cur_solution)
            cur_solution = self.divide(cur_solution, self.matrix[row][row])
            self.solution[row] = cur_solution

    def calculate_error(self):
        error = []
        for variable_index in range(self.SIZE):
            error.append(abs(self.solution[variable_index] - self.prev_solution[variable_index]))
        return GaussSeidelIteration(self.solution, error)

    def solve(self):
        self.check_diagonal_dominant()
        for iteration in range(self.iterations):
            self.do_iteration()
            self.iterations_list.append(self.calculate_error())
            self.prev_solution = copy.deepcopy(self.solution)
            if self.iterations_list[-1].max_error < self.precision:
                break
        return self.solution
