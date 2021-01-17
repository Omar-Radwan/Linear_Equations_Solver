NUMBER_OF_EQUATION_INDEX=0
METHOD_INDEX=1
FIRST_EQUATION_INDEX=2


class ReadFromFile():

    def __init__(self):
        file=open("input","r")
        self.lines=file.read().splitlines()
        self.seidel_initial_index=FIRST_EQUATION_INDEX+self.number_of_equations()

    def number_of_equations(self):
        return int(self.lines[NUMBER_OF_EQUATION_INDEX])

    def get_method(self):
        return self.lines[METHOD_INDEX]

    def get_equation_list(self):
        equation_list=self.lines[FIRST_EQUATION_INDEX:FIRST_EQUATION_INDEX+self.number_of_equations()]
        return equation_list

    def get_seidel_initial(self):
        seidel_initial=self.lines[self.seidel_initial_index].split(" ")
        seidel_initial = [float(i) for i in seidel_initial]

        return seidel_initial
