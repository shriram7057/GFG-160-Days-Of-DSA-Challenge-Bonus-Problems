class Solution:
    def targetSumComb(self, arr, target):
        # code here
        arr.sort()
        res=[]
        def backtrack(i,curr,total):
            if total == target:
                res.append(curr[:])
                return 
            if total > target or i == len(arr):
                return 
            curr.append(arr[i])
            backtrack(i,curr,total+arr[i])
            curr.pop()
            
            backtrack(i+1,curr,total)
        backtrack(0,[],0)
        return res