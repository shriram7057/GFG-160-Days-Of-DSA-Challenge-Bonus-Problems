class Solution:
    def romanToDecimal(self, s): 
        # code here
        roman={
            'I':1,'V':5,'X':10,'L':50,
            'C':100,'D':500,'M':1000
        }
        total=0
        n=len(s)
        
        for i in range(n):
            if i+1 < n and roman[s[i]]< roman[s[i+1]]:
                total-=roman[s[i]]
            else:
                total += roman[s[i]]
        return total 