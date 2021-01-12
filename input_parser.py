import re

from gauss_elimination import GaussianElimination
from matrix_solver import print_matrix

TERM_PATTERN = r'([+-][\d]{0,}[\.?[\d]{0,}]{0,}[*]?[a-zA-Z]?)'
NUMBER_PATTERN = r'([-+]?\d+[\.?[\d]{0,}]{0,})'
VARIABLE_ONLY=1
NUMBER_ONLY=2
NUMBER_AND_VARIABLE=3

class InputParser:

    def get_inputs(self,list_of_equations):
        self.prepare_equations(list_of_equations)
        index_dictionary=self.index_dictionary(list_of_equations)
        matrix,results=self.get_coefficient_matrix(list_of_equations,index_dictionary)
        return index_dictionary,matrix,results


    #type 1:single variable,type 2:single number,type 3:variable with number
    def get_type(self,splitted_term):
        if len(splitted_term)==1:
            if self.is_digit(splitted_term[0]):
                return NUMBER_ONLY
            else :
                return VARIABLE_ONLY
        else :
            return NUMBER_AND_VARIABLE

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
        #print(equations)

    def get_coefficient_matrix(self, list_of_equations: list,index_dictionary):

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

                if self.get_type(splitted_term)==VARIABLE_ONLY:
                    coefficient = self.sign_of_variable(splitted_term)
                    splitted_term = splitted_term[0][1]
                    matrix[i][index_dictionary[splitted_term[0]]] = coefficient

                elif self.get_type(splitted_term)==NUMBER_ONLY:
                    results[i] = float(splitted_term[0]) * -1

                else :
                    coefficient = splitted_term[0]
                    matrix[i][index_dictionary[splitted_term[1]]] = float(coefficient)

        return matrix, results

    # return index dictionary.
    def index_dictionary(self, list_of_equations):

        dictionaryIndex = {}
        i = 0

        for equation in list_of_equations:
            terms = re.findall(TERM_PATTERN, equation)

            for term in terms:
                splitted_term = term.split('*')
                if self.get_type(splitted_term) == VARIABLE_ONLY:
                     variable = splitted_term[0][1]
                     dictionaryIndex,i=self.put_in_dictionary(dictionaryIndex,i,variable)
                elif self.get_type(splitted_term) ==NUMBER_AND_VARIABLE:
                     variable = splitted_term[1]
                     dictionaryIndex,i=self.put_in_dictionary(dictionaryIndex,i,variable)



        print(dictionaryIndex)
        return dictionaryIndex


    def put_in_dictionary(self,dictionary_index:{},i,variable):
        if not variable in dictionary_index.keys():
            dictionary_index[variable] = i
            i += 1
        return dictionary_index,i


"""input_parser = InputParser()
list_of_equations = ["25*a+5*b+c-106.8", "64*a+8*b+c-177.2", "144*a+12*b+c-279.2","4*a+12*b+c+f-279.2",
                     "4*a+12*b+c+f+z-279.2"]
input_parser.get_inputs(list_of_equations)
input_parser.prepare_equations(list_of_equations)
matrix, results = input_parser.get_coefficient_matrix(list_of_equations)
gaussian_elemination = GaussianElimination(matrix, results)
print(gaussian_elemination.solve())
print_matrix(gaussian_elemination.matrix)
print(matrix)
print(results)"""
