class Solution:
    def lowerBound(self, arr, target):
        # code here
        l,r=0,len(arr)
        
        while l < r:
            mid = (l+r)//2
            if arr[mid]< target:
                l=mid+1
            else:
                r=mid
        return l