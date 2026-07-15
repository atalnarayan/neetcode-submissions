class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = [[] for _ in range(n)]
        
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        def bfs(queue):
            while queue:
                node = queue.popleft()
                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
        
        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                visited.add(node)
                bfs(deque([node]))
        
        return count

