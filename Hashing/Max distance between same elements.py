class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        first={}
        ans=0
        
        for i , val in enumerate(arr):
            if val not in first:
                first[val]=i
            else:
                ans=max(ans,i-first[val])
        return ans