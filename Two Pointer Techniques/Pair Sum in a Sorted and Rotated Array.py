#User function Template for python3

class Solution:
    ##Complete this function
    def pairInSortedRotated(self,arr, target):
        #Your code here
        n=len(arr)
        pivot=0
        for i in range(1,n):
            if arr[i] < arr[i-1]:
                pivot = i
                break
        l=pivot
        r=(pivot-1) % n
        while l != r:
            s=arr[l] + arr[r]
            if s == target:
                return True
            elif s < target:
                l=(l+1) % n
            else:
                r = (r-1+n) % n
        return False
                