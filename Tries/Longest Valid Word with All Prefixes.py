class Solution:
    def longestValidWord(self, words):
        # code here 
        wordset=set(words)
        best=""
        
        for w in words:
            valid=True
            for i in range(1,len(w)):
                if w[:i] not in wordset:
                    valid=False
                    break
            if valid:
                if len(w)>len(best)or(len(w)==len(best)and w<best):
                    best=w
        return best