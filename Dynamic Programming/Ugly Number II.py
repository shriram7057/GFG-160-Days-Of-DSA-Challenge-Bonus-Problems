class Solution:
    # Function to find the nth ugly number.
    def uglyNumber(self, n):
        # code here
        dp=[0]*n
        dp[0]=1
        i2=i3=i5=0
        
        for i in range(1,n):
            next2=dp[i2]*2
            next3=dp[i3]*3
            next5=dp[i5]*5
            
            nxt=min(next2,next3,next5)
            dp[i]=nxt
            
            if nxt == next2:
                i2 += 1
            if nxt == next3:
                i3 += 1
            if nxt == next5:
                i5 += 1
        return dp[-1]