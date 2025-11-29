class Solution:
    def subsets(self, arr):
        # code here
        res=[]
        n=len(arr)
        def backtrack(i,curr):
            if i == n:
                res.append(curr[:])
                return
            backtrack(i+1,curr)
            curr.append(arr[i])
            backtrack(i+1,curr)
            curr.pop()
        backtrack(0,[])
        return res