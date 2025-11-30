class Solution:
    def possibleWords(self, arr):
        # code here
        mapping={
            2:"abc",3:"def",4:"ghi",5:"jkl",
            6:"mno",7:"pqrs",8:"tuv",9:"wxyz"
        }
        n=len(arr)
        res=[""]
        for digit in arr:
            if digit not in mapping:
                continue
            temp=[]
            for prefix in res:
                for ch in mapping[digit]:
                    temp.append(prefix+ch)
            res=temp
        return res