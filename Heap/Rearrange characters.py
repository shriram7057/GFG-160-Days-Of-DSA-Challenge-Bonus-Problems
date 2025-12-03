import heapq
class Solution :
    def rearrangeString(self, s):
        #code here
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        maxHeap = []
        
        for ch, f in freq.items():
            heapq.heappush(maxHeap,(-f,ch))
        
        prev = (0,'')
        result = []
        
        while maxHeap:
            f, ch = heapq.heappop(maxHeap)
            result.append(ch)
            
            if prev[0] < 0:
                heapq.heappush(maxHeap,prev)
            
            prev=(f+1,ch)
        
        res="".join(result)
        
        if len(res) != len(s):
            return ""
        return res