class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = [[] for _ in range(n)]

        for node, nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)
        
        def check_cycle_dfs(node, parent):
            if node in visited:
                return True
            
            visited.add(node)

            for nei in adj[node]:
                if nei != parent:
                    if check_cycle_dfs(nei, node):
                        return True
            
            return False
            
        has_cycle = check_cycle_dfs(0, -1)
        
        return not has_cycle and len(visited) == n



