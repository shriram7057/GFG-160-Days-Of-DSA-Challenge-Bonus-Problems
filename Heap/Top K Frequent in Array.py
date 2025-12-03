class Solution:
	def topKFreq(self, arr, k):
		# Code here
	    from collections import Counter
	    import heapq
	    
	    freq = Counter(arr)
	    
	    heap = [(-f,-num) for num, f in freq.items()]
	    heapq.heapify(heap)
	    
	    result = []
	    
	    for _ in range(k):
	        f,num = heapq.heappop(heap)
	        result.append(-num)
	    return result