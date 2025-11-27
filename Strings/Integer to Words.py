#User function Template for python3

class Solution:
    def convertToWords(self, n):
        # code here 
        ones=["","One ","Two ","Three ","Four ","Five ","Six ","Seven ","Eight ","Nine ","Ten ","Eleven ","Twelve ","Thirteen ","Fourteen ","Fifteen ","Sixteen ",
        "Seventeen ","Eighteen ","Nineteen "]
        tens=["","","Twenty ","Thirty ","Forty ","Fifty ","Sixty ","Seventy ","Eighty ","Ninety "]
        
        def two_digits(num):
            if num < 20:
                return ones[num]
            return tens[num//10]+ones[num%10]
        
        def three_digits(num):
            if num==0:
                return ""
            if num < 100:
                return two_digits(num)
            return ones[num//100] + "Hundred " + two_digits(num % 100)
        if n==0:
            return "Zero"
        result=""
        
        billion = n // 1000000000
        if billion:
            result += three_digits(billion) + "Billion "
        n%=1000000000
        
        million = n // 1000000
        if million:
            result += three_digits(million) + "Million "
        n %= 1000000
        
        thousand = n // 1000
        if thousand:
            result += three_digits(thousand) + "Thousand "
        n %= 1000
        
        hundred = n // 100
        if hundred:
            result += ones[hundred] + "Hundred "
        n %= 100
        if n:
            if result !="":
                result +=""
            result += two_digits(n)
        return result.strip()
    