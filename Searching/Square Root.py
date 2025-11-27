class Solution:
    def floorSqrt(self, n): 
        # code here
        l,r=0,n
        ans=0
        while l <= r:
            mid=(l+r)//2
            if mid * mid <= n:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans