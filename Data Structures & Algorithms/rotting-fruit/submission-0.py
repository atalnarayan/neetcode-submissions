class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def bfs(queue, fresh_count):
            mins = 0
            while queue:
                num_level_elems = len(queue)
                made_one_stale = False

                for _ in range(num_level_elems):
                    (i,j) = queue.popleft()

                    for (x,y) in [(i+1, j), (i-1,j), (i, j+1), (i, j-1)]:
                        if 0<=x<m and 0<=y<n and grid[x][y] == 1:
                            grid[x][y] = 2
                            if not made_one_stale:
                                mins += 1
                                made_one_stale = True
                            fresh_count -= 1
                            queue.append((x,y))
            
            return mins, fresh_count


        
        queue = deque([])
        fresh_count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh_count += 1
        
        mins, fresh_count = bfs(queue, fresh_count)

        # check whether there's a fresh fruit still
        return mins if not fresh_count else -1
