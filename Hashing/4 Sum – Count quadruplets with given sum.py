class Solution:
    def countSum(self, arr, target):
        #code here
        arr.sort()
        n=len(arr)
        count=0
        seen=set()
        
        for i in range(n-3):
            for j in range(i+1,n-2):
                left=j+1
                right=n-1
                
                while left < right:
                    s=arr[i]+arr[j]+arr[left]+arr[right]
                    
                    if s== target:
                        quad=(arr[i],arr[j],arr[left],arr[right])
                        if quad not in seen:
                            seen.add(quad)
                            count+=1
                            right-=1
                        elif s<target:
                            left+=1
                        else:
                            right-=1
        return count