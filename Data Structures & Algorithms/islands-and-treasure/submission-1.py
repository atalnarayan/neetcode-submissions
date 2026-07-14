class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        INF = 2147483647
        queue = deque()
        
        # 1. Enqueue all initial treasure coordinates
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    
        # Define directions once to save memory reallocation
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 2. Flattened BFS
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and if the cell is unvisited (INF)
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == INF:
                    # The distance is just the current cell's value + 1!
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))