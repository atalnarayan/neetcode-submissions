class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1]*n
        parent = list(range(n))
        components = n

        def find_root(node):
            p = parent[node]
            while parent[p] != p:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p


        
        def union(x,y):
            root_x, root_y = find_root(x), find_root(y)

            if root_x == root_y:
                return 0
        
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
                rank[root_x] += rank[root_y]
            
            else:
                parent[root_x] = root_y
                rank[root_y] += rank[root_x]
            
            return 1
            
        for x,y in edges:
            components -= union(x,y)
        
        return components

