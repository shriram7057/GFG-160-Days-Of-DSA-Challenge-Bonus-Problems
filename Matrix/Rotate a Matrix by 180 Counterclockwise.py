class Solution:
	def rotateMatrix(self, mat):
		# Code here
		n=len(mat)
		m=len(mat[0])
		
		for i in range(n):
		    mat[i].reverse()
		mat.reverse()
		return mat