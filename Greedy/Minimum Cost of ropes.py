import heapq
class Solution:
   def minCost(self, arr):
    # code here
    if len(arr)<=1:
        return 0
    heapq.heapify(arr)
    total=0
    
    while len(arr) > 1:
        a=heapq.heappop(arr)
        b=heapq.heappop(arr)
        cost= a+b
        total += cost
        heapq.heappush(arr,cost)
    return total