class Solution:
    def kokoEat(self, arr, k):
        # Code here
        def canEat(speed):
            hours= 0
            for p in arr:
                hours += (p+speed-1)// speed
            return hours <= k
        l,r=1,max(arr)
        ans=r
        
        while l<= r:
            mid=(l+r)//2
            if canEat(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans