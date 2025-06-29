from collections import defaultdict, deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[n-1][n-1] !=0 or grid[0][0] !=0 : return -1

        dirs = [(0,1),(1,0), (1,1), (-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]

        Q = deque()
        Q.append([0,0,1])

        while Q:

            x,y, d = Q.popleft()
            if (x,y) == (n-1, n-1) : 
                return d

            for dx, dy in dirs:
                x2,y2= x+dx, y+dy
                if 0<=x2<n and 0<=y2<n :
                    if grid[x2][y2]==0 :
                        Q.append([x2,y2, d+1])
                        grid[x2][y2] = 1

        return -1
                
            





        