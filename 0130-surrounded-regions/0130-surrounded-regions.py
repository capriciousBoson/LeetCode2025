from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def show(board):
            for row in board:
                print(row)
        print(f"initial board : - ")
        show(board)
        m, n = len(board), len(board[0])

        visited = [[False for _ in range(n)] for __ in range(m)]

        Q = deque()
        reverse  = []
        for i in range(m):
            for j in range(n):
                if board[i][j] =="O" and ((i in(0, m-1) )or (j in(0, n-1))):
                    Q.append((i,j))
                    visited[i][j] = True
                    board[i][j] = 1
                    reverse.append((i,j))

        print(f"after marking boundayr Os --- ")
        show(board)
        print(f"\nQ : {Q}")
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while Q:
            i,j = Q.popleft()
            print(f"\n reached : {i,j} - ---------------------------------------")
            for dx, dy in dirs:
                x,y = i+dx, j+dy
                print(f"exploring : {x,y} ------------------")
                if 0<=x<m and 0<=y<n and board[x][y]=="O" and not visited[x][y]:
                    print(f"marking : {x,y}")
                    board[x][y] = 1
                    reverse.append((x,y))
                    Q.append((x,y))
                    visited[x][y] = True
        print(f"\nafter bfs ---")
        show(board)
        for i in range(1,m):
            for j in range(1,n):
                if board[i][j]=="O": board[i][j] = "X"

        for i,j in reverse:
            board[i][j] = "O"
        return board


        