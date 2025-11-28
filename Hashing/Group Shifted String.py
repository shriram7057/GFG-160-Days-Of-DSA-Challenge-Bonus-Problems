class Solution:
    def groupShiftedString(self, arr):
        #code here
        groups={}
        for s in arr:
            if len(s)==1:
                key="single"
            else:
                key=[]
                for i in range(1,len(s)):
                    diff=(ord(s[i])- ord(s[i-1])) % 26
                    key.append(diff)
                key=tuple(key)
            if key not in groups:
                groups[key]=[]
            groups[key].append(s)
        return list(groups.values())