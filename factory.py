from gauss_elimination import GaussianElimination
from gauss_seidel import GaussSeidel
from gauss_jordan import GaussJordan
from lu_decomposition import LuDecomposition

class Factory():

    def method_type(self,matrix,result,method,seidel_initials):

        if method=="Guass Elimination":
            return [GaussianElimination(matrix,result)]

        elif method=="Guass Jordan":
            return [GaussJordan(matrix,result)]

        elif method=="Guass Seidel":
            return [GaussSeidel(matrix,result,seidel_initials)]

        elif method=="LU decomposition":
            return [LuDecomposition(matrix,result)]

        elif method=="All":
            return [GaussSeidel(matrix,result),GaussianElimination(matrix,result),GaussJordan(matrix,result),
                    LuDecomposition(matrix,result)]


