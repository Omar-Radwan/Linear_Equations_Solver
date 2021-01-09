import re

from gauss_elimination import GaussianElimination
from matrix_solver import print_matrix

TERM_PATTERN = r'([+-][\d]{0,}[\.?[\d]{0,}]{0,}[*]?[a-zA-Z]?)'
NUMBER_PATTERN = r'([-+]?\d+[\.?[\d]{0,}]{0,})'


class InputParser:

    def is_digit(self, n):
        return bool(re.fullmatch(NUMBER_PATTERN, n))

    def sign_of_variable(self, string):
        if string[0][0] == '+':
            return 1
        return -1

    def prepare_equations(self, equations: [str]):
        for i in range(len(equations)):

            if len(equations[i]) != 0 and equations[i][0] != '+' and equations[i][0] != '-':
                equations[i] = equations[i].replace(" ", "")
                equations[i] = f'+{equations[i]}'
        print(equations)

    def get_coefficient_matrix(self, list_of_equations: list):

        index_dictionary = self.index_dictionary(list_of_equations)

        number_of_equations = len(list_of_equations)
        matrix = [[0 for j in range(number_of_equations)] for i in range(number_of_equations)]
        results = [0 for j in range(number_of_equations)]

        for i in range(len(list_of_equations)):

            equation = list_of_equations[i]
            terms = re.findall(TERM_PATTERN, equation)

            for term in terms:

                splitted_term = term.split('*')
                # +1231.123*c ... +c ... +1231231
                # variable with coefficient = 1 or just single number
                if len(splitted_term) == 1:

                    # check if single number
                    if self.is_digit(splitted_term[0]):
                        results[i] = float(splitted_term[0]) * -1
                    # variable with coefficient =1
                    else:
                        coefficient = self.sign_of_variable(splitted_term)
                        splitted_term = splitted_term[0][1]
                        matrix[i][index_dictionary[splitted_term[0]]] = coefficient


                else:
                    coefficient = splitted_term[0]
                    matrix[i][index_dictionary[splitted_term[1]]] = float(coefficient)

        return matrix, results

    # The equation which have all variables.
    def is_complete_equation(self, terms, number_of_variables):

        if len(terms) == number_of_variables + 1:
            return True

        elif len(terms) == number_of_variables:
            for term in terms:
                splitted_term = term.split('*')
                if len(splitted_term) == 1 and self.is_digit(splitted_term[0]):
                    return False
            return True

        return False

    # return index dictionary.
    def index_dictionary(self, list_of_equations):

        dictionaryIndex = {}
        number_of_variables = len(list_of_equations)

        for equation in list_of_equations:
            terms = re.findall(TERM_PATTERN, equation)

            if self.is_complete_equation(terms, number_of_variables):

                for i in range(len(terms)):
                    term = terms[i]
                    splitted_term = term.split('*')

                    # variable with coefficient = 1
                    if len(splitted_term) == 1:  # digit or variable +12312, -c
                        if not self.is_digit(splitted_term[0]):
                            variable = splitted_term[0][1]
                        else:
                            continue
                    else:
                        variable = splitted_term[1]

                    dictionaryIndex[variable] = i

                break
        print(dictionaryIndex)
        return dictionaryIndex


input_parser = InputParser()
list_of_equations = ["25*a+5*b+c-106.8", "64*a+8*b+c-177.2", "144*a+12*b+c-279.2"]
input_parser.prepare_equations(list_of_equations)
matrix, results = input_parser.get_coefficient_matrix(list_of_equations)
gaussian_elemination = GaussianElimination(matrix, results)
print(gaussian_elemination.solve())
print_matrix(gaussian_elemination.matrix)
print(matrix)
print(results)
