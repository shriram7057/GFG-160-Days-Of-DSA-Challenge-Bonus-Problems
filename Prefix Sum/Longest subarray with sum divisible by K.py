#User function Template for python3
class Solution:
	def longestSubarrayDivK(self, arr, k):
		#Complete the function
        prefix_mod ={}
        prefix_mod[0]= -1 
        s = 0
        ans = 0
        
        for i , x in enumerate(arr):
            s += x
            m = s % k
            
            if m in prefix_mod:
                ans = max(ans,i - prefix_mod[m])
            else:
                prefix_mod[m] = i 
        return ans
