class Solution:
    def minDaysBloom(self, arr, k, m):
        # Code here
        if len(arr)< m * k:
            return -1
        def canMake(days):
            bouquets=0
            flowers=0
            
            for bloom in arr:
                if bloom <= days:
                    flowers += 1
                    if flowers == k :
                        bouquets += 1
                        flowers=0
                else:
                    flowers = 0 
            return  bouquets >= m
        l , r = min(arr),max(arr)
        ans = -1
        while l <= r:
            mid=(l+r)//2
            if canMake(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans