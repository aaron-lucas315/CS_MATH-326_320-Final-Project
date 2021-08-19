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
                 
                # Evaluating L(i, j)using L(j, j)
                for k in range(j):
                    sum1 += (lower[i][k] *lower[j][k]);
                if(lower[j][j] > 0):
                    lower[i][j] = round((matrix[i][j] - sum1) / lower[j][j], 3);
 
    # Displaying Lower Triangular and its Transpose
    print("Lower Triangular\t\tTranspose");
    for i in range(n):
         
        # Lower Triangular
        for j in range(n):
            print(lower[i][j], end = "\t");
        print("", end = "\t");
         
        # Transpose of
        # Lower Triangular
        for j in range(n):
            print(lower[j][i], end = "\t");
        print("");

# Driver Code
n=3
A = np.random.randint(10, size =(n, n))
matrix = np.dot(A, A.transpose())
print(matrix)
Cholesky_Decomposition(matrix, n)
