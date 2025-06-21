from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # visited = [[0 for _ in range(cols)] for __ in range(rows)]


        Q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    # visited[i][j]==1
                    Q.append((i,j,0))

        dr = [(0,1), (1,0), (0,-1), (-1,0)]
        minutes = 0

        while Q:
            i,j,m = Q.popleft()
            minutes = max(minutes, m)

            for dx, dy in dr:
                x = i+dx
                y = j+dy

                if 0<=x<rows and 0<=y<cols:
                    if grid[x][y] == 1 :
                        Q.append((x,y,m+1))
                        grid[x][y] = 2
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        return minutes
        
                    







        