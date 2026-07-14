class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def bfs(queue):
            visited = {(i,j) for (i,j) in queue}
            while queue:
                num_level_elems = len(queue)
                for _ in range(num_level_elems):
                    (i,j) = queue.popleft()

                    for (x,y) in [(i-1, j), (i+1, j), (i, j-1), (i,j+1)]:
                        if 0<=x<m and 0<=y<n and heights[x][y] >= heights[i][j] and (x,y) not in visited:
                            visited.add((x,y))
                            queue.append((x,y))
            return visited
                        
        
        pacific_queue = deque(((0,j) for j in range(n)))
        pacific_queue.extend(((i,0) for i in range(1, m)))
        pacific_set = bfs(pacific_queue)

        atlantic_queue = deque(((m-1,j) for j in range(n)))
        atlantic_queue.extend(((i,n-1) for i in range(m-1)))
        atlantic_set = bfs(atlantic_queue)

        common_set = atlantic_set.intersection(pacific_set)

        return [[i,j] for (i,j) in common_set]