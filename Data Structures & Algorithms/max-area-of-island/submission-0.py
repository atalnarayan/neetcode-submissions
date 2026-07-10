class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m, n, max_area = len(grid), len(grid[0]), 0

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n and grid[i][j] == 1):
                return 0
            grid[i][j] = -1
            return 1 + dfs(i-1,j)+ dfs(i+1,j)+ dfs(i, j+1) + dfs(i, j-1)
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    max_area = max(area, max_area)
        
        return max_area

