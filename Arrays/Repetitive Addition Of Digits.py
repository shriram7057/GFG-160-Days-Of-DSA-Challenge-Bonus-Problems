class Solution:
    def singleDigit(self, n):
    	#code here 
    	if n==0:
            return 0
    	r= n % 9
    	return 9 if r == 0 else r 