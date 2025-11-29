class Solution:
    def isBipartite(self, V, edges):
        # code here
        adj=[[]for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        color=[-1]*V
        
        from collections import deque
        
        for i in range(V):
            if color[i]== -1:
                q=deque([i])
                color[i]=0
                
                while q:
                    node=q.popleft()
                    for nei in adj[node]:
                        if color[nei]== -1:
                            color[nei]=1 - color[node]
                            q.append(nei)
                        elif color[nei]== color[node]:
                            return False
        return True