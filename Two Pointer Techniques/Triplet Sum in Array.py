class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        arr.sort()
        n=len(arr)
        
        for i in range(n-2):
            l = i + 1
            r = n - 1
            
            while l < r:
                s=arr[i] + arr[l] + arr[r]
                
                if s == target:
                    return True
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return False