class Solution:
    def maxOnes(self, arr, k):
        # code here
        left = 0
        zero_count=0
        ans=0
        
        for right in range(len(arr)):
            if arr[right]==0:
                zero_count+=1
            while zero_count>k:
                if arr[left]==0:
                    zero_count -= 1
                left += 1
            ans = max(ans,right - left + 1)
        return ans