from methods.gauss_elimination import GaussianElimination
from methods.gauss_seidel import GaussSeidel
from methods.gauss_jordan import GaussJordan
from methods.lu_decomposition import LuDecomposition
from methods.gauss_elimination_pivoting import GaussianEliminationPivoting
class Factory():

    def method_type(self,matrix,result,method,seidel_initials):

        if method=="Guass Elimination":
            return [GaussianElimination(matrix,result)]

        elif method=="Guass Elimination-pivoting":
            return [GaussianEliminationPivoting(matrix,result)]

        elif method=="Guass Jordan":
            return [GaussJordan(matrix,result)]

        elif method=="Guass Seidel":
            return [GaussSeidel(matrix,result,seidel_initials)]

        elif method=="LU decomposition":
            return [LuDecomposition(matrix,result)]

        elif method=="All":
            return [GaussSeidel(matrix,result,seidel_initials),GaussianElimination(matrix,result),GaussJordan(matrix,result),
                    LuDecomposition(matrix,result),GaussianEliminationPivoting(matrix,result)]


