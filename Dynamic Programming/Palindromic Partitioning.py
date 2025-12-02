#User function Template for python3

class Solution:
    def palPartition(self, s):
        # code here
        n=len(s)
        pal=[[False]*n for _ in range(n)]
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<2 or  pal[i+1][j-1]):
                    pal[i][j]=True
        dp=[0]*(n+1)
        dp[n]= -1
        
        for i in range(n-1,-1,-1):
            best=float('inf')
            for j in range(i,n):
                if pal[i][j]:
                    best=min(best,1 + dp[j+1])
            dp[i]=best
        return dp[0]