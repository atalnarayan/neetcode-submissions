class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        nei_delta = [(-1,0), (1,0), (0,-1), (0,1)]

        def bfs(queue):
            while queue:
                (i,j) = queue.popleft()

                for dr,dc in nei_delta:
                    x,y = i+dr,j+dc
                    if 0<=x<m and 0<=y<n and board[x][y] != 'V' and board[x][y] == 'O':
                        board[x][y] = 'V'
                        queue.append((x,y))

        
        queue = deque([])
        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i,0))
                board[i][0] = 'V'

            if board[i][n-1] == 'O':
                queue.append((i,n-1))
                board[i][n-1] = 'V'
        
        for j in range(1, n-1):
            if board[0][j] == 'O':
                queue.append((0,j))
                board[0][j] = 'V'

            if board[m-1][j] == 'O':
                queue.append((m-1, j))
                board[m-1][j] = 'V'
        
        bfs(queue)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        


