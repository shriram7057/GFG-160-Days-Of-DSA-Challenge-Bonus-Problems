class Solution:
    def catchThieves(self, arr, k):
        #code here
        policeman=[]
        thieves=[]
        
        for i,ch in enumerate(arr):
            if ch =='P':
                policeman.append(i)
            else:
                thieves.append(i)
        i=j=0
        caught=0
        
        while i < len(policeman) and j < len(thieves):
            if abs(policeman[i]-thieves[j]) <= k:
                caught+=1
                i+=1
                j+=1
            elif policeman[i] < thieves[j]:
                i+=1
            else:
                j+=1
        return caught

s