class Solution:
    def celebrity(self, mat):
        # code here
        n=len(mat)
        
        a=0
        b=n-1
        while a<b:
            if mat[a][b] == 1:
                a += 1
            else:
                b -= 1
        celeb = a
        
        for i in range(n):
            if i == celeb:
                continue
            if mat[celeb][i] == 1 or mat[i][celeb] == 0:
                return -1
        return celeb