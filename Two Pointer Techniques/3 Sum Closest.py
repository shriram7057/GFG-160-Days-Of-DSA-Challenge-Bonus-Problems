class Solution:
    def closest3Sum(self, arr, target):
        # code here
        arr.sort()
        n=len(arr)
        
        bestSum=float('-inf')
        closestDiff=float('inf')
        
        for i in range(n-2):
            l,r=i+1,n-1
            
            while l < r:
                s=arr[i]+arr[l]+arr[r]
                diff = abs(s-target)
                
                if diff < closestDiff or (diff == closestDiff and s > bestSum):
                    closestDiff = diff
                    bestSum = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s
        return bestSum