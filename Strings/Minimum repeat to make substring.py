class Solution:
    def minRepeats(self, s1, s2):
        # code here 
        rep=s1
        count=1
        while len(rep)<len(s2):
            rep += s1
            count += 1
        if s2 in rep:
            return count
        rep += s1
        if s2 in rep:
            return count + 1
        return -1