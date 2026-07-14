class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        nei_delta = [(-1,0), (1,0), (0,-1), (0,1)]

        def bfs(queue, visited):
            while queue:
                (i,j) = queue.popleft()

                for dr,dc in nei_delta:
                    x,y = i+dr,j+dc
                    if 0<=x<m and 0<=y<n and not visited[x][y] and board[x][y] == 'O':
                        visited[x][y] = True
                        queue.append((x,y))


        visited = [[False for _ in range(n)] for _ in range(m)]
        
        queue = deque([])
        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i,0))
                visited[i][0] = True

            if board[i][n-1] == 'O':
                queue.append((i,n-1))
                visited[i][n-1] = True
        
        for j in range(1, n-1):
            if board[0][j] == 'O':
                queue.append((0,j))
                visited[0][j] = True

            if board[m-1][j] == 'O':
                queue.append((m-1, j))
                visited[m-1][j] = True
        
        bfs(queue, visited)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'

        


