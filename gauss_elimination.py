class GaussianElimination:
    def __init__(self, matrix: [], result: []):
        self.matrix = matrix
        self.result = result
        self.SIZE = len(matrix)
        self.solution = [0 for i in range(self.SIZE)]

    def obtain_zero(self, row: int, col: int, pivot_row: int):
        # TODO: check for division by 0
        if (self.matrix[row][col] == 0):
            return True
        ratio = (-self.matrix[row][col] / self.matrix[pivot_row][col])
        for cur_col in range(self.SIZE + 1):
            self.matrix[row][cur_col] += ratio * self.matrix[pivot_row][cur_col]

    def build_lower_zeros(self):
        for row in range(self.SIZE - 1, 0, -1):
            self.obtain_zero(row, 0, 0)
        for col in range(1, self.SIZE - 1):
            for row in range(self.SIZE - 1, col, -1):
                self.obtain_zero(row, col, row - 1)

    def back_substitution(self):
        for col in range(self.SIZE - 1, -1, -1):
            cur_solution = (self.result[col] / self.matrix[col][col])
            self.solution[col] = cur_solution
            for row in range(col, -1, -1):
                self.result[row] -= (cur_solution * self.matrix[row][col])

    def build_augmented_matrix(self):
        for row in range(self.SIZE):
            self.matrix[row].append(self.result[row])

    def build_results_array(self):
        for row in range(self.SIZE):
            self.result[row] = self.matrix[row][-1]
            self.matrix[row].pop()

    def solve(self):
        self.build_augmented_matrix()
        self.build_lower_zeros()
        self.build_results_array()
        self.back_substitution()
        return self.solution
