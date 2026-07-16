class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1]*n
        parent = list(range(n))
        components = n

        def find(node) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(u,v) -> int:
        
            root_u, root_v = find(u), find(v)

            if root_u == root_v:
                return 0

            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            
            elif rank[root_v] < rank[root_u] :
                parent[root_u] = root_v
            
            else:
                parent[root_v] = root_u
                rank[root_u] += 1
            
            return 1
        
        for u,v in edges:
            components -= union(u,v)
        
        return components
            


