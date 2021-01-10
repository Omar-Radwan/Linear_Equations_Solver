from main import gui
from input_parser import InputParser
from factory import Factory
from matrix_solver import MatrixSolver

class controller:

    def begin(self):
        equation_list,method_string=self.get_input()
        matrix,results=self.parse_input(equation_list)
        method_object=self.method_type(matrix,results,method_string)
        self.solve(method_object)

    def get_input(self):
        gui_object = gui()
        gui_object.begin()
        equation_list = gui_object.equationsList
        method = gui_object.method.get()
        return equation_list,method

    def parse_input(self,equation_list):
        input_parser = InputParser()
        matrix,results=input_parser.get_coefficient_matrix(equation_list)
        return matrix,results

    def method_type(self,matrix,results,method_string):
        factory=Factory()
        method=factory.method_type(matrix,results,method_string)
        return method

    def solve(self,method_object):
        print(method_object.solve())
        #to be sent to output gui


c=controller()
c.begin()



