class Solution:
    def nextGreater(self, arr):
        # code here
        n=len(arr)
        res=[-1] * n
        stack=[]
        
        for i in range(2 * n):
            cur = arr[i % n]
            
            while stack and arr[stack[-1]] < cur:
                res[stack.pop()] = cur
            
            if i < n:
                stack.append(i)
        return res