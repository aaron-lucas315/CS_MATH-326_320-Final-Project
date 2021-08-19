import timeit

mysetup = """
import numpy as np

def luDecomposition(mat, n):

	lower = [[0 for x in range(n)]
			for y in range(n)]
	upper = [[0 for x in range(n)]
			for y in range(n)]

	# Decomposing matrix into Upper and Lower triangular matrix
	for i in range(n):

		# Upper Triangular
		for k in range(i, n):

			# Summation of L(i, j) * U(j, k)
			sum = 0
			for j in range(i):
				sum += (lower[i][j] * upper[j][k])

			# Evaluating U(i, k)
			upper[i][k] = mat[i][k] - sum

		# Lower Triangular
		for k in range(i, n):
			if (i == k):
				lower[i][i] = 1 # Diagonal as 1
			else:

				# Summation of L(k, j) * U(j, i)
				sum = 0
				for j in range(i):
					sum += (lower[k][j] * upper[j][i])

				# Evaluating L(k, i)
				lower[k][i] = round((mat[k][i] - sum) / upper[i][i], 3)
"""

mycode = """
n=128
matrix = np.random.randint(10, size =(n, n))
luDecomposition(matrix, n)
"""
time = 0
for i in range(100):
    time += timeit.timeit(setup=mysetup, stmt=mycode, number=1)
print("Average runtime: ", round(time/100,3))
