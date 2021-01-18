from main import gui
from input_parser import InputParser
from factory import Factory
# from output import Output
import time
from read_from_file import ReadFromFile
from output import Output

class Controller:

    def begin(self):
        iterations_list = []
        equation_list, method_string, seidel_initials,iterations,precision = self.get_input()

        method_list=[method_string]
        index_dictionary, matrix, results = self.parse_input(equation_list)
        print("matrix",matrix)
        method_object = self.method_type(matrix, results, method_string, seidel_initials,iterations,precision)
        roots, total_time,errors = self.solve(method_object)
        if method_string == "Guass Seidel" :
            iterations_list = method_object[0].iterations_list
        elif method_string=="All":
            iterations_list = method_object[0].iterations_list
            method_list=["Guass Seidel","Guass Elimination", "Guass Jordan",  "LU decomposition","Guass Elimination-pivoting"]

        self.display_output(roots, "100", total_time, index_dictionary, iterations_list,method_list,errors)

    def get_input(self):
        gui_object = gui()
        gui_object.begin()
        iterations=50
        precision=0.00001
        if gui_object.read_from_file:
            read_from_file = ReadFromFile()
            equation_list = read_from_file.get_equation_list()
            method = read_from_file.get_method()
            sidel_initials=""
            if method=="All" or method=="Guass Seidel":
                sidel_initials=read_from_file.get_seidel_initial()

        else:
            equation_list = gui_object.equationsList
            method = gui_object.method.get()
            sidel_initials = gui_object.initials
            iterations=gui_object.maximumIterations.get()
            precision=gui_object.precision.get()
        return equation_list, method, sidel_initials,iterations,precision

    def parse_input(self, equation_list):
        input_parser = InputParser()
        index_dictionary, matrix, results = input_parser.get_inputs(equation_list)
        return index_dictionary, matrix, results

    def method_type(self, matrix, results, method_string, seidel_initials,iterations,precision):
        factory = Factory()
        method = factory.method_type(matrix, results, method_string, seidel_initials,iterations,precision)
        return method

    def solve(self, method_object):
        roots = []
        total_time = []
        errors=[0 for i in range(len(method_object))]
        for i in range(len(method_object)):
            t1 = time.time()

            roots.append(method_object[i].solve())
            errors[i]=method_object[i].error


            total_time.append(time.time() - t1)
        return roots, total_time,errors


    def display_output(self, roots, precision, total_time, index_dictionary, iterations_list,method_list,errors):
        output = Output()
        output.begin(total_time, roots, index_dictionary, iterations_list,method_list,errors, precision)
