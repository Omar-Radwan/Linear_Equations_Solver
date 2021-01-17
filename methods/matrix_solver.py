import copy
import heapq

from constants import *


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
    def __init__(self, matrix: [], result: [], iterations=50):
        self.matrix = copy.deepcopy(matrix)
        self.result = copy.deepcopy(result)
        self.SIZE = len(self.matrix)
        self.iterations = iterations
        self.has_error = False
        self.error = ""

    def build_lower_zeros(self):
        """
            function that builds lower zeroes
            ***     ***
            *** ->  0**
            ***     00*
            Complexity O(n^3)
        """
        for row in range(self.SIZE - 1, 0, -1):
            self.__obtain_zero(row, 0, 0)

        for col in range(1, self.SIZE - 1):
            for row in range(self.SIZE - 1, col, -1):
                self.__obtain_zero(row, col, row - 1)

    def build_lower_zeros_with_pivoting(self):
        """
            function that builds lower zeroes and applies pivoting

            ***     ***
            *** ->  0**
            ***     00*
            Complexity O(n^3)
        """
        self.__apply_pivoting(0, self.SIZE - 1, 0)
        for row in range(self.SIZE - 1, 0, -1):
            self.__obtain_zero(row, 0, 0)

        for col in range(1, self.SIZE - 1):
            self.__apply_pivoting(col + 1, self.SIZE - 1, col)
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
            self.check_solvability(self.matrix[col][col], self.result[col])
            self.result[col] = self.divide(self.result[col], self.matrix[col][col])
            for row in range(col - 1, -1, -1):
                self.result[row] -= (self.result[col] * self.matrix[row][col])
        return self.result

    def forward_substitution(self):
        for col in range(0, self.SIZE):
            self.check_solvability(self.matrix[col][col], self.result[col])
            self.result[col] = self.divide(self.result[col], self.matrix[col][col])
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

    def obtain_ones_in_the_main_diagonal(self):
        for row in range(self.SIZE):
            self.check_solvability(self.matrix[row][row], self.matrix[row][-1])
            self.matrix[row][-1] = self.divide(self.matrix[row][-1], self.matrix[row][row])
            self.matrix[row][row] = self.divide(self.matrix[row][row], self.matrix[row][row])

    def divide(self, numerator, denominator):
        if denominator == 0:
            if not self.has_error:
                self.has_error = True
                self.error = DIVISION_BY_ZERO
            return 1
        else:
            return numerator / denominator

    def check_diagonal_dominant(self):
        for i in range(self.SIZE):
            row_sum = 0
            for j in range(self.SIZE):
                if i != j:
                    row_sum += abs(self.matrix[i][j])
            if abs(self.matrix[i][i]) < row_sum:
                if not self.has_error:
                    self.has_error = True
                    self.error = NOT_DIAGONALLY_DOMINANT

    def check_pivot_row(self, row):
        all_zeros = True
        for i in range(self.SIZE):
            if self.matrix[row][i] != 0:
                all_zeros = False
                break

        if all_zeros:
            self.check_solvability(0, self.matrix[row][-1])

    def check_solvability(self, coefficient, result):
        if coefficient == 0:
            if result == 0:
                if not self.has_error:
                    self.has_error = True
                    self.error = INFINITE_SOLUTIONS

            else:
                if not self.has_error:
                    self.has_error = True
                    self.error = NO_SOLUTION

    def __obtain_zero(self, row: int, col: int, pivot_row: int):
        if self.matrix[row][col] == 0:
            return
        self.check_pivot_row(pivot_row)
        ratio = self.divide(-self.matrix[row][col], self.matrix[pivot_row][col])
        for cur_col in range(len(self.matrix[row])):
            self.matrix[row][cur_col] += ratio * self.matrix[pivot_row][cur_col]

    def __apply_pivoting(self, from_row, to_row, column):
        sorted_indices = []
        old_matrix = copy.deepcopy(self.matrix)
        for row in range(from_row, to_row + 1):
            heapq.heappush(sorted_indices, (-self.matrix[row][column], row))

        for row in range(from_row, to_row + 1):
            max_row_index = heapq.heappop(sorted_indices)[1]
            self.matrix[row] = old_matrix[max_row_index]

    def solve(self):
        pass
