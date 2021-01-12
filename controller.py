from main import gui
from input_parser import InputParser
from factory import Factory
from matrix_solver import MatrixSolver
from output import Output
import time
from read_from_file import ReadFromFile
from output_all import OutputAll

class controller:

    def begin(self):

        equation_list,method_string=self.get_input()
        index_dictionary,matrix,results=self.parse_input(equation_list)
        method_object=self.method_type(matrix,results,method_string)
        t1 = time.time()
        roots=self.solve(method_object)
        totalTime = time.time() - t1
        self.display_output(roots,"100",totalTime,index_dictionary)

    def get_input(self):
        gui_object = gui()
        gui_object.begin()
        if gui_object.read_from_file:
            read_from_file=ReadFromFile()
            equation_list=read_from_file.get_equation_list()
            method=read_from_file.get_method()

        else:
            equation_list = gui_object.equationsList
            method = gui_object.method.get()
        return equation_list,method

    def parse_input(self,equation_list):
        input_parser = InputParser()
        index_dictionary,matrix,results=input_parser.get_inputs(equation_list)
        return index_dictionary,matrix,results

    def method_type(self,matrix,results,method_string):
        factory=Factory()
        method=factory.method_type(matrix,results,method_string)
        return method

    def solve(self,method_object):
        roots=[]
        for i in range(len(method_object)):
            roots.append(method_object[i].solve())
        return roots

    def display_output(self,roots,precision,time,index_dictionary):
        if len(roots)>1:
            output=OutputAll()
        else:
            output = Output()
        output.begin(time, roots, precision, index_dictionary)


c=controller()
c.begin()



