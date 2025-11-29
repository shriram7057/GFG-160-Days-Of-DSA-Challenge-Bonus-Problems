class Solution:
    def getComponents(self, V, edges):
        # code here
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited=[False]*V
        components=[]
        
        def dfs(node,comp):
            visited[node]=True
            comp.append(node)
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei,comp)
        for i in range(V):
            if not visited[i]:
                comp=[]
                dfs(i,comp)
                components.append(comp)
        return components