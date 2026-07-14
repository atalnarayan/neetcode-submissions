class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        pacific = [[False for _ in range(n)] for _ in range(m)]
        atlantic = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i,j,visited):
            visited[i][j] = True

            for dr,dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                x,y = i+dr,j+dc
                if 0<=x<m and 0<=y<n and not visited[x][y] and heights[x][y] >= heights[i][j]:
                    visited[x][y] = True
                    dfs(x,y, visited)
        
        for i in range(m):
            dfs(i,0, pacific)
        for j in range(1, n):
            dfs(0,j, pacific)

        for i in range(m):
            dfs(i,n-1, atlantic)
        for j in range(n-1):
            dfs(m-1,j, atlantic)
        
        return [[i,j] for i in range(m) for j in range(n) if pacific[i][j] and atlantic[i][j]]