class Solution:
    # Function to count the number of subarrays with a sum that is divisible by K
    def subCount(self, arr, k):
        # Your code goes here
        freq = {0:1}
        s= 0
        ans = 0
        
        for x in arr:
            s += x
            m = s % k
            if m in freq:
                ans += freq[m]
                freq[m] += 1
            else:
                freq[m] = 1
        return ans