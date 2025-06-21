from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])

        
        Q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and ((i in (0,m-1)) or (j in (0,n-1))):
                    Q.append((i,j))
                    grid[i][j] = -1
        # print(f"Q : {Q}")
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        while Q:
            i,j = Q.popleft()

            for dx, dy in dirs:
                x,y = i+dx, j+dy
                if 0<=x<m and 0<=y<n and grid[x][y]==1 :
                    Q.append((x,y))
                    grid[x][y] = -1
                    

        # for r in grid: print(r)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += 1
        return ans

        


        