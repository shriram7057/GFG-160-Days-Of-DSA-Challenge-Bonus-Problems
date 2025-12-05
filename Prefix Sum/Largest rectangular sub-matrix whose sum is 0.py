from typing import List

class Solution:
    def zeroSumSubmat(self, mat):
        # code here
        n=len(mat)
        m=len(mat[0])
        
        pref=[[0]*(m+1) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                pref[i][j+1] = pref[i][j] + mat[i][j]
        ans = 0
        
        for left in range(m):
            for right in range(left,m):
                comp=[]
                for i in range(n):
                    comp.append(pref[i][right+1] - pref[i][left])
                s=0
                seen = {0: -1}
                
                for i in range(n):
                    s += comp[i]
                    if s in seen:
                        height = i - seen[s]
                        width = right - left + 1
                        ans=max(ans,height * width)
                    else:
                        seen[s] = i
                        
        return ans               
