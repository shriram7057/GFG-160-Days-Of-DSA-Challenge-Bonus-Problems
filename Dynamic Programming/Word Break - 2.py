#User function Template for python3

class Solution:
    def wordBreak(self, dict, s):
        # code here
        wordset=set(dict)
        memo={}
        
        def solve(i):
            if i==len(s):
                return [""]
            if i in memo:
                return memo[i]
            res=[]
            for j in range(i+1,len(s)+1):
                word=s[i:j]
                if word in wordset:
                    subs=solve(j)
                    
                    for sub in subs:
                        if sub == "":
                            res.append(word)
                        else:
                            res.append(word + " " + sub)
            memo[i]=res
            return res
        return solve(0)