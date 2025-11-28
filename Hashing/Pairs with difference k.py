#User function Template for python3
class Solution:
	def countPairs(self, arr, k):
    	# code here
        freq={}
        for x in arr:
            freq[x]=freq.get(x,0)+1
        count=0
        
        if k==0:
            for v in freq.values():
                if v > 1:
                    count += (v*(v-1))//2
        else:
            for x in freq:
                if x+k in freq:
                    count  += freq[x]*freq[x+k]
        return count
