class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False]*n
        adj = [[] for _ in range(n)]
        
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        def dfs(node):
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        count = 0
        for node in range(n):
            if not visited[node]:
                count += 1
                visited[node] = True
                dfs(node)
        
        return count
