class Solution:
    def balanceSums(self, mat):
        # code here
        n=len(mat)
        
        row=[sum(mat[i]) for i in range(n)]
        col=[sum(mat[i][j] for i in range(n)) for j in range(n)]
        
        maxSum = max(max(row),max(col))
        
        totalSum=sum(row)
        
        return maxSum * n - totalSum