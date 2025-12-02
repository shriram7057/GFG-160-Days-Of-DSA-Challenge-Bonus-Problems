#User function Template for python3

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self, n, k):
        # code here
        # def eggDrop(self,n,k):
        dp=[0]*(n+1)
        moves=0
            
        while dp[n]<k:
            moves += 1
            for e in range(n,0,-1):
                dp[e]=dp[e]+dp[e-1]+1
        return moves