class Solution:
    def generateMatrix(self, rowSum, colSum):
        # code here
        n=len(rowSum)
        m=len(colSum)
        
        mat=[[0]*m for _ in range(n)]
        
        i=0
        j=0
        
        while i < n and j < m:
            val=min(rowSum[i],colSum[j])
            mat[i][j]=val
            
            rowSum[i] -= val
            colSum[j] -= val
            
            if rowSum[i]==0:
                i+=1
            if colSum[j]==0:
                j+=1
        return mat