class Solution:
    def minRemovals(self, arr, k):
        # code here
        total = sum(arr)
        target = total - k
        
        if target < 0:
            return -1
        if target == 0:
            return len(arr)
        n=len(arr)
        l = 0
        curr = 0
        max_len = -1
        
        for i in range(n):
            curr += arr[i]
            while curr > target:
                curr -= arr[l]
                l += 1
            if curr == target:
                max_len = max(max_len, i - l + 1 )
        if max_len == -1:
            return -1
        return n - max_len
