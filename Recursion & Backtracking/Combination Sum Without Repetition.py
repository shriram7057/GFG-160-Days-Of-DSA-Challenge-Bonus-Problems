class Solution:
    def uniqueCombinations(self, arr, target):
        # code here
        arr.sort()
        res=[]
        comb=[]
        
        def backtrack(start,remaining):
            if remaining == 0:
                res.append(list(comb))
                return
            if remaining < 0:
                return 
            for i in range(start,len(arr)):
                if i > start and arr[i]==arr[i-1]:
                    continue
                if arr[i] > remaining:
                    break
                comb.append(arr[i])
                backtrack(i+1,remaining-arr[i])
                comb.pop()
        backtrack(0,target)
        return res