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


def double_cmp(a, b):
    return abs(a - b) < 1


def compare_matrices(a, b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if not double_cmp(a[i][j], b[i][j]):
                return False
    return True


class MatrixSolver():
    def __init__(self, matrix: [], result: [], iterations=50):
        self.old_matrix = copy.deepcopy(matrix)
        self.old_result = copy.deepcopy(result)

        self.matrix = copy.deepcopy(matrix)
        self.result = copy.deepcopy(result)
        self.SIZE = len(self.matrix)
        self.iterations = iterations
        self.has_error = False
        self.error = ""

    def build_lower_zeros(self):
        """
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
            builds lower zeroes and applies pivoting
            ***     ***
            *** ->  0**
            ***     00*
            Complexity O(n^3)
        """
        self.__apply_pivoting(0, self.SIZE - 1, 0)
        for row in range(self.SIZE - 1, 0, -1):
            self.__obtain_zero(row, 0, 0)

        for col in range(1, self.SIZE - 1):
            self.__apply_pivoting(col, self.SIZE - 1, col)
            for row in range(self.SIZE - 1, col, -1):
                self.__obtain_zero(row, col, row - 1)

    def build_upper_zeros(self):
        """
            ***     *00
            *** ->  **0
            ***     ***
            Complexity O(n^3)
        """
        for row in range(0, self.SIZE - 1):
            self.__obtain_zero(row, self.SIZE - 1, self.SIZE - 1)

        for col in range(self.SIZE - 2, 0, -1):
            for row in range(0, col):
                self.__obtain_zero(row, col, row + 1)

    def back_substitution(self):
        """
            calculates the value of each variable starting from the last row till the first row
            Complexity O(n^2)
        """
        for col in range(self.SIZE - 1, -1, -1):
            self.check_solvability(self.matrix[col][col], self.result[col])
            self.result[col] = self.divide(self.result[col], self.matrix[col][col])
            for row in range(col - 1, -1, -1):
                self.result[row] -= (self.result[col] * self.matrix[row][col])
        return self.result

    def forward_substitution(self):
        """
            calculates the value of each variable starting from the first row till the last row
            Complexity O(n^2)
        """
        for col in range(0, self.SIZE):
            self.check_solvability(self.matrix[col][col], self.result[col])
            self.result[col] = self.divide(self.result[col], self.matrix[col][col])
            for row in range(col + 1, self.SIZE):
                self.result[row] -= (self.result[col] * self.matrix[row][col])
        return self.result

    def build_augmented_matrix(self):
        """
           connects the coefficients matrix and the results matrix in one matrix (augmented matrix)
        """
        for row in range(self.SIZE):
            self.matrix[row].append(self.result[row])

    def separate_augmented_matrix(self):
        """
           separates the coefficients and results matrix from the augmented matrix
        """
        for row in range(self.SIZE):
            self.result[row] = self.matrix[row][-1]
            self.matrix[row].pop()

    def obtain_ones_in_the_main_diagonal(self):
        """
            divides each row from result by the coefficient of main diagonal element in that row
        """
        for row in range(self.SIZE):
            self.check_solvability(self.matrix[row][row], self.matrix[row][-1])
            self.matrix[row][-1] = self.divide(self.matrix[row][-1], self.matrix[row][row])
            self.matrix[row][row] = self.divide(self.matrix[row][row], self.matrix[row][row])

    def divide(self, numerator, denominator):
        """
            applies numerator/denominator if denominator is not 0
        """
        if denominator == 0:
            if not self.has_error:
                self.has_error = True
                self.error += DIVISION_BY_ZERO
            return 1
        else:
            return numerator / denominator

    def check_diagonal_dominant(self):
        """
            checks if matrix is not diagonal dominant
        """

        for i in range(self.SIZE):
            row_sum = 0
            for j in range(self.SIZE):
                if i != j:
                    row_sum += abs(self.matrix[i][j])
            if abs(self.matrix[i][i]) < row_sum:
                if not self.has_error:
                    self.error += NOT_DIAGONALLY_DOMINANT + ', '
                    return

    def check_pivot_row(self, row):
        """
            checks if the pivot row is all zeros in this case number of solutions infinite
        """
        all_zeros = True
        for i in range(self.SIZE):
            if self.matrix[row][i] != 0:
                all_zeros = False
                break

        if all_zeros:
            self.check_solvability(0, self.matrix[row][-1])

    def check_solvability(self, coefficient, result):
        """
             checks if there is infinite number of solutions or that there's no solution
        """
        if coefficient == 0:
            if result == 0:
                if not self.has_error:
                    self.has_error = True
                    self.error += INFINITE_SOLUTIONS

            else:
                if not self.has_error:
                    self.has_error = True
                    self.error += NO_SOLUTION

    def __obtain_zero(self, row: int, col: int, pivot_row: int):
        """
            takes row and col of element and obtains zero in position matrix[row][col] using pivot row provided
        """
        if self.matrix[row][col] == 0:
            return
        self.check_pivot_row(pivot_row)
        ratio = self.divide(-self.matrix[row][col], self.matrix[pivot_row][col])
        for cur_col in range(len(self.matrix[row])):
            self.matrix[row][cur_col] += ratio * self.matrix[pivot_row][cur_col]

    def __apply_pivoting(self, from_row, to_row, column):
        """
            functions that sorts rows of matrix in range(from_row, to_row) according to absolute value of column in descending order
        """
        sorted_indices = []
        old_matrix = copy.deepcopy(self.matrix)
        for row in range(from_row, to_row + 1):
            heapq.heappush(sorted_indices, (-abs(self.matrix[row][column]), row))
        for row in range(from_row, to_row + 1):
            max_row_index = heapq.heappop(sorted_indices)[1]
            self.matrix[row] = old_matrix[max_row_index]

    def solve(self):
        for i in range(self.SIZE):
            res = 0
            for j in range(self.SIZE):
                res += self.result[j] * self.old_matrix[i][j]
            if not double_cmp(res, self.old_result[i]):
                print(res, self.old_result[i])
