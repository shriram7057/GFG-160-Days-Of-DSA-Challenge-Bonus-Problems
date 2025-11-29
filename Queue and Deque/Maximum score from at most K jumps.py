import heapq
class Solution:
    def getScore(self, arr, k):
        # code here
        n=len(arr)
        dp=[0]*n
        dp[0]=arr[0]
        
        maxheap=[(-dp[0],0)]
        
        for i in range(1,n):
            while maxheap and maxheap[0][1]<i-k:
                heapq.heappop(maxheap)
            dp[i]=arr[i]+(-maxheap[0][0])
            
            heapq.heappush(maxheap,(-dp[i],i))
        return dp[-1]