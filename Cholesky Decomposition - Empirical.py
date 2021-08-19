import timeit

mysetup = """
import math
import numpy as np

def Cholesky_Decomposition(matrix, n):
 
    lower = [[0 for x in range(n + 1)]
            for y in range(n + 1)];
 
    # Decomposing a matrix into Lower Triangular
    for i in range(n):
        for j in range(i + 1):
            sum1 = 0;
 
            # sum1mation for diagnols
            if (j == i):
                for k in range(j):
                    sum1 += pow(lower[j][k], 2);
                lower[j][j] = round(math.sqrt(abs(matrix[j][j] - sum1)), 3);
            else:
                 
                # Evaluating L(i, j) using L(j, j)
                for k in range(j):
                    sum1 += (lower[i][k] *lower[j][k]);
                if(lower[j][j] > 0):
                    lower[i][j] = round((matrix[i][j] - sum1) / lower[j][j], 3);
"""

mycode = """
n=128
A = np.random.randint(10, size =(n, n))
matrix = np.dot(A, A.transpose())
Cholesky_Decomposition(matrix, n)
"""
time = 0
for i in range(100):
    time += timeit.timeit(setup=mysetup, stmt=mycode, number=1)
print("Average runtime: ", round(time/100,3))
