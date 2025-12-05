#User function Template for python3
class Solution:
    def touchedXaxis(self, arr):
        # code here
        pos = 0
        count = 0
        
        for delta in arr:
            prev = pos
            pos += delta
            
            if pos == 0 or(prev < 0 and pos > 0) or (prev> 0 and pos <0):
                count += 1
        return count 
        