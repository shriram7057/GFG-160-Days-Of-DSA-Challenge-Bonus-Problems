#User function Template for python3

class Solution:
    def minIncrements(self, arr): 
        # Code here
        arr.sort()
        moves=0
        
        for i in range(1,len(arr)):
            if arr[i] <= arr[i-1]:
                needed=arr[i-1]+1
                moves+=needed - arr[i]
                arr[i]=needed
        return moves