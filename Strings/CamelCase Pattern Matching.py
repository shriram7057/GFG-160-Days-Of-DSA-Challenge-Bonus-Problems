#User function Template for python3

class Solution:
    def camelCase(self,arr,pat):
        #code here
        res=[]
        for w in arr:
            caps= "".join(c for c in  w if c.isupper())
            if caps.startswith(pat):
                res.append(w)
        return res 