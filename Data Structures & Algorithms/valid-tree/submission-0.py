class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = [[] for _ in range(n)]
        
        for node, nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)

        def dfs(node, parent):
            for nei in adj[node]:
                if nei == parent:
                    continue
                
                if nei in visited:
                    return True

                visited.add(nei)
                if dfs(nei, node):
                    return True
            
            return False
            
        visited.add(0)
        has_cycle = dfs(0, -1)

        return not has_cycle and len(visited) == n

