# Create a spiral matrix of N*M size from given array
#User function Template for python3
class Solution:
    def spiralFill(self, n, m, arr):
        # code here
        mat=[[0]*m for _ in range(n)]
        
        top,bottom=0,n-1
        left,right=0,m-1
        idx=0
        while top <= bottom and left <= right:
            
            for j in range(left,right+1):
                mat[top][j]=arr[idx]
                idx+=1
            top += 1
            
            for i in range(top,bottom+1):
                mat[i][right]=arr[idx]
                idx+=1
            right -= 1
            
            if top <= bottom:
                for j in range(right,left-1,-1):
                    mat[bottom][j]=arr[idx]
                    idx += 1
                bottom -= 1
            if left <= right:
                for i in range(bottom,top-1,-1):
                    mat[i][left]=arr[idx]
                    idx+=1
                left +=1
        return mat