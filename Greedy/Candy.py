class Solution:
    def minCandy(self, arr):
        # Code here
        n=len(arr)
        if n==1:
            return 1
        left=[1]*n
        right=[1]*n
        
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                left[i]=left[i-1]+1
        for i in range(n-2,-1,-1):
            if arr[i]>arr[i+1]:
                right[i]=right[i+1]+1
        total=0
        for i in range(n):
            total += max(left[i],right[i])
        return total