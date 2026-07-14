class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid), len(grid[0])
        INF = 2147483647

        def bfs(queue):
            while queue:
                (i,j) = queue.popleft()
    
                for (x,y) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if (0<=x<m) and (0<=y<n) and grid[x][y] == INF:
                        grid[x][y] = grid[i][j] + 1
                        queue.append((x,y)) 

        queue = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j))
        bfs(queue)
                              
