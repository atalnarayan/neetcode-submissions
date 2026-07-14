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
            for j in (0,n-1):
                if board[i][j] == 'O':
                    queue.append((i,j))
                    board[i][j] = 'V'

        
        for j in range(1, n-1):
            for i in [0,m-1]:
                if board[i][j] == 'O':
                    queue.append((i,j))
                    board[i][j] = 'V'
        
        bfs(queue)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        


