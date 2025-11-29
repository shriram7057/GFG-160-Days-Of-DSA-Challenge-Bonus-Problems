#User function Template for python3
class Solution:
    def totHammingDist(self, arr):
        # code here
        n=len(arr)
        ans=0
        
        for bit in range(32):
            ones=0
            mask=1<<bit
            for x in arr:
                if x & mask:
                    ones += 1
            zeros=n-ones
            ans += ones*zeros
        return ans