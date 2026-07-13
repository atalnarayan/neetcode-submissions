"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = dict()
        visited[node] = Node(node.val)

        def dfs(curr):
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    dfs(neighbor)
                visited[curr].neighbors.append(visited[neighbor])
            return visited[curr]
        
        
        return dfs(node)
