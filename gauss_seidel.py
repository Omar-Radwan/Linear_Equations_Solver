import copy

from gauss_seidel_iteration import GaussSeidelIteration
from matrix_solver import MatrixSolver


class GaussSeidel(MatrixSolver):
    def __init__(self, matrix: [], result: [], initials, iterations=50):
        super().__init__(matrix, result)
        print("inin", initials)
        self.iterations_list = []
        self.prev_solution = []
        if len(initials) == 0:
            self.solution = [0 for i in range(self.SIZE)]
        else:
            self.solution = copy.deepcopy(initials)

    def do_iteration(self):
        for row in range(self.SIZE):
            cur_solution = self.result[row]
            for col in range(self.SIZE):
                if row != col:
                    cur_solution -= (self.solution[col] * self.matrix[row][col])
            cur_solution = self.divide(cur_solution, self.matrix[row][row])
            self.solution[row] = cur_solution

    def calculate_error(self):
        error = []
        for variable_index in range(self.SIZE):
            error.append(abs(self.solution[variable_index] - self.prev_solution[variable_index]))
        return GaussSeidelIteration(self.solution, error)

    def solve(self):
        for iteration in range(self.iterations + 1):
            self.do_iteration()
            if iteration > 0:
                self.iterations_list.append(self.calculate_error())
            self.prev_solution = copy.deepcopy(self.solution)
        return self.solution
