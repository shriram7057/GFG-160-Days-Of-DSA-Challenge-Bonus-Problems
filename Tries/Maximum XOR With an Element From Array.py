class TrieNode:
    def __init__(self):
        self.child=[None,None]
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,num):
        curr=self.root
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            if not curr.child[bit]:
                curr.child[bit]=TrieNode()
            curr=curr.child[bit]
    def maxXor(self,num):
        curr=self.root
        ans=0
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            opp=1-bit
            if curr.child[opp]:
                ans |= (1 << i)
                curr=curr.child[opp]
            else:
                curr=curr.child[bit]
        return ans
class Solution:
    def maxXor(self,arr,queries):
        arr.sort()
        q=len(queries)
        
        offline=[]
        for i in range(q):
            xi,mi=queries[i]
            offline.append((mi,xi,i))
        offline.sort()
        
        t=Trie()
        idx=0
        n=len(arr)
        ans=[-1]*q
        
        for mi,xi,qi in offline:
            while idx<n and arr[idx]<=mi:
                t.insert(arr[idx])
                idx+=1
            if idx==0:
                ans[qi]=-1
            else:
                ans[qi]=t.maxXor(xi)
        return ans