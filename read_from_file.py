NUMBER_OF_EQUATION_INDEX=0
METHOD_INDEX=1
FIRST_EQUATION_INDEX=2

class ReadFromFile():

    def __init__(self):
        file=open("input","r")
        self.lines=file.read().splitlines()

    def number_of_equations(self):
        return int(self.lines[NUMBER_OF_EQUATION_INDEX].strip())

    def get_method(self):
        return self.lines[METHOD_INDEX].strip()

    def get_equation_list(self):
        equation_list=self.lines[FIRST_EQUATION_INDEX:FIRST_EQUATION_INDEX+self.number_of_equations()]
        return equation_list
