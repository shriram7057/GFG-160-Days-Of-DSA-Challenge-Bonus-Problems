class Solution:
    def subsetXORSum(self, arr):
        # code here
        n=len(arr)
        OR=0
        for x in arr:
            OR |= x
        return OR * (1<<(n-1))