import heapq
class Solution:
    def minMeetingRooms(self, start, end):
        # code here
        n=len(start)
        
        meetings=sorted(zip(start,end))
        heap=[]
        
        for s,e in meetings:
            if heap and heap[0] <= s:
                heapq.heappop(heap)
            heapq.heappush(heap,e)
        return len(heap)
            
