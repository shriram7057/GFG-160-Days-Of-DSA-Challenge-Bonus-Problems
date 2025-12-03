import heapq
class Solution:
    def mostBooked(self, n, meetings):
        # code here
        meetings.sort()
        
        free = list(range(n))
        heapq.heapify(free)
        
        busy=[]
        
        count = [0] * n
        
        for start, end in meetings:
            while busy and busy[0][0] <= start:
                endTime,room = heapq.heappop(busy)
                heapq.heappush(free,room)
            duration = end - start
            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy,(end,room))
                count[room] += 1
            else:
                endTime , room=heapq.heappop(busy)
                newEnd=endTime + duration
                heapq.heappush(busy,(newEnd,room))
                count[room] += 1
        maxMeetings = max(count)
        for i in range(n):
            if count[i] == maxMeetings:
                return i
                
    