#User function Template for python3
class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        total=sum(arr)
        if total % 3 != 0:
            return[-1,-1]
        part=total//3
        s=0
        first=-1
        second=-1
        for i in range(len(arr)):
            s+=arr[i]
            if s==part and first==-1:
                first=i
            elif s==2 * part and first!=-1:
                second=i
                break
        if first != -1 and second != -1 and second < len(arr)-1:
            return[first,second]
        return[-1,-1]