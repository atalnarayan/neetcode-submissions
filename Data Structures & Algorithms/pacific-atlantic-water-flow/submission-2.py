class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def bfs(queue):
            visited = [[False for j in range(n)] for i in range(m)]
            while queue:
                num_level_elems = len(queue)
                for _ in range(num_level_elems):
                    (i,j) = queue.popleft()
                    visited[i][j] = True

                    for (x,y) in [(i-1, j), (i+1, j), (i, j-1), (i,j+1)]:
                        if 0<=x<m and 0<=y<n and heights[x][y] >= heights[i][j] and not visited[x][y]:
                            visited[x][y] = True
                            queue.append((x,y))
            return visited
                        
        
        pacific_queue = deque(((0,j) for j in range(n)))
        pacific_queue.extend(((i,0) for i in range(1, m)))
        pacific = bfs(pacific_queue)

        atlantic_queue = deque(((m-1,j) for j in range(n)))
        atlantic_queue.extend(((i,n-1) for i in range(m-1)))
        atlantic = bfs(atlantic_queue)

        return [(i,j) for i in range(m) for j in range(n) if pacific[i][j] and atlantic[i][j]]