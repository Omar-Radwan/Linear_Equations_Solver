import copy


def multiply(mat_a: [], mat_b: []):
    p1, q1, p2, q2 = len(mat_a), len(mat_a[0]), len(mat_b), len(mat_b[0])
    assert q1 == p2
    result = [[0 for j in range(q2)] for i in range(p1)]
    for i in range(p1):
        for j in range(q1):
            result[i][j] = sum(mat_a[i][k] * mat_b[k][j] for k in range(p2))
    return result


def print_matrix(mat_a: []):
    for x in mat_a:
        print(x)


class MatrixSolver():
    def __init__(self, matrix: [], result: [],iterations=50):
        self.matrix = copy.deepcopy(matrix)
        self.result = copy.deepcopy(result)
        self.SIZE = len(self.matrix)
        self.iterations = iterations


    def __obtain_zero(self, row: int, col: int, pivot_row: int):
        # TODO: check for division by 0
        if self.matrix[row][col] == 0:
            return True
        ratio = (-self.matrix[row][col] / self.matrix[pivot_row][col])
        for cur_col in range(len(self.matrix[row])):
            self.matrix[row][cur_col] += ratio * self.matrix[pivot_row][cur_col]

    def build_lower_zeros(self):
        for row in range(self.SIZE - 1, 0, -1):
            self.__obtain_zero(row, 0, 0)
        for col in range(1, self.SIZE - 1):
            for row in range(self.SIZE - 1, col, -1):
                self.__obtain_zero(row, col, row - 1)

    def build_upper_zeros(self):
        for row in range(0, self.SIZE - 1):
            self.__obtain_zero(row, self.SIZE - 1, self.SIZE - 1)

        for col in range(self.SIZE - 2, 0, -1):
            for row in range(0, col):
                self.__obtain_zero(row, col, row + 1)

    def back_substitution(self):
        for col in range(self.SIZE - 1, -1, -1):
            self.result[col] /= self.matrix[col][col]
            for row in range(col - 1, -1, -1):
                self.result[row] -= (self.result[col] * self.matrix[row][col])
        return self.result

    def forward_substitution(self):
        for col in range(0, self.SIZE):
            self.result[col] /= self.matrix[col][col]
            for row in range(col + 1, self.SIZE):
                self.result[row] -= (self.result[col] * self.matrix[row][col])
        return self.result

    def build_augmented_matrix(self):
        for row in range(self.SIZE):
            self.matrix[row].append(self.result[row])

    def separate_augmented_matrix(self):
        for row in range(self.SIZE):
            self.result[row] = self.matrix[row][-1]
            self.matrix[row].pop()

    def obtain_main_diagonal_ones(self):
        for row in range(self.SIZE):
            divisor = self.matrix[row][row]
            for col in range(len(self.matrix[row])):
                self.matrix[row][col] /= divisor



    def solve(self):
        pass
