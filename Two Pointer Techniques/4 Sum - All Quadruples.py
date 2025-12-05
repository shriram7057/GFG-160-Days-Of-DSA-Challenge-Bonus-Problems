class Solution:
    def fourSum(self, arr, target):
        # code here
        arr.sort()
        n=len(arr)
        res=[]
        
        for i in range(n-3):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            for j in range(i+1,n-2):
                if j > i + 1 and arr[j] == arr[j-1]:
                    continue
                l=j+1
                r=n-1
                
                while l < r:
                    s=arr[i]+arr[j]+arr[l]+arr[r]
                
                    if s == target:
                        res.append([arr[i],arr[j],arr[l],arr[r]])
                    
                        l += 1
                        r -= 1
                    
                        while l < r and arr[l] == arr[l-1]:
                            l += 1
                        while l < r and arr[r] == arr[r+1]:
                            r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        return res
        