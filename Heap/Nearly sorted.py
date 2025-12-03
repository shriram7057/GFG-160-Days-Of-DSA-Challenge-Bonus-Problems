import heapq
class Solution:
    def nearlySorted(self, arr, k):  
        #code here
        n=len(arr)
        heap = []
        
        for i in range(min(k+1,n)):
            heapq.heappush(heap,arr[i])
        idx = 0
        
        for i in range(k+1,n):
            arr[idx]= heapq.heappop(heap)
            idx += 1
            heapq.heappush(heap, arr[i])
            
        while heap:
            arr[idx] = heapq.heappop(heap)
            idx += 1