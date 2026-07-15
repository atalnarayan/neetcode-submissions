class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # more edges ==> cycle
        # less edges ==> not connected
        if len(edges) != n-1:
            return False

        # if the graph is indeed connected, then one should be able to visit all of the nodes
        visited = set()
        adj = [[] for _ in range(n)]


        for node, nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)
        
        def check_connected(queue):
            while queue:
                node = queue.popleft()

                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            
        queue = deque([0])
        visited.add(0)
        check_connected(queue)
        
        return len(visited) == n



