class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
        m, n, count = len(grid), len(grid[0]), 0

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n and grid[i][j] == "1"):
                return
            grid[i][j] = "*"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    area = dfs(i,j)
                    
        
        return count