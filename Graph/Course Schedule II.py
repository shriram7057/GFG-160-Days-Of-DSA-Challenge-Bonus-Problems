class Solution:
    def findOrder(self, n, prerequisites):
        # code here 
        adj=[[]for _ in range(n)]
        indeg=[0]*n
        
        for x,y in prerequisites:
            adj[y].append(x)
            indeg[x]+=1
        
        from collections import deque
        q=deque()
        for i in range(n):
            if indeg[i]==0:
                q.append(i)
        order=[]
        
        while q:
            node=q.popleft()
            order.append(node)
            
            for nei in adj[node]:
                indeg[nei]-=1
                if indeg[nei]==0:
                    q.append(nei)
        if len(order)==n:
            return order
        return []
