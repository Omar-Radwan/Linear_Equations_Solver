from gauss_elimination import GaussianElimination

mat = [[1, 2, 3],
       [0, -7, -11],
       [-6, -8, 1]]
result = [-7, 23, -22]
gaussian_elimination = GaussianElimination(mat, result)
gaussian_elimination.solve()
print(gaussian_elimination.solution)
