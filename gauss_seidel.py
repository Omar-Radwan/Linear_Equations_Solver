from matrix_solver import MatrixSolver


class GaussSeidel(MatrixSolver):
    def __init__(self, matrix: [], result: [], iterations=50):
        super().__init__(matrix, result)
        self.solution = [0 for i in range(self.SIZE)]
        self.iterations = iterations

    def do_iteration(self):
        for row in range(self.SIZE):
            cur_solution = self.result[row]
            for col in range(self.SIZE):
                if row != col:
                    cur_solution -= (self.solution[col] * self.matrix[row][col])
            cur_solution /= self.matrix[row][row]
            self.solution[row] = cur_solution

    def solve(self):
        for i in range(self.iterations):
            self.do_iteration()
        return self.solution
