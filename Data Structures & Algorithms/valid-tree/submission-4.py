class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = [[] for _ in range(n)]

        for node, nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)
        
        def check_cycle_bfs(queue):
            while queue:
                node, parent = queue.popleft()

                for nei in adj[node]:
                    if nei == parent:
                        continue
                
                    if nei in visited:
                        return True
                    
                    visited.add(nei)
                    queue.append((nei, node))
                
            return False
            
        queue = deque([(0,-1)])
        visited.add(0)
        has_cycle = check_cycle_bfs(queue)
        
        return not has_cycle and len(visited) == n



