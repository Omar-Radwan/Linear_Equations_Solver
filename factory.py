from gauss_elimination import GaussianElimination
from gauss_seidel import GaussSeidel
from gauss_jordan import GaussJordan
from lu_decomposition import LuDecomposition

class Factory():

    def method_type(self,matrix,result,method):

        if method=="Guass Elimination":
            return GaussianElimination(matrix,result)

        elif method=="Guass Jordan":
            return GaussJordan(matrix,result)

        elif method=="Guass Seidel":
            return GaussSeidel(matrix,result)

        elif method=="LU decomposition":
            return LuDecomposition(matrix,result)


