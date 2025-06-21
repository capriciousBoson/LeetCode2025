from collections import deque
from copy import deepcopy
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m,n = len(mat), len(mat[0])
        Q = deque()

        res = deepcopy(mat)
        visited = [[False for _ in range(n)] for __ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] ==0:
                    visited[i][j] = True
                    Q.append((i,j,0))
        

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while Q:
            i, j, d = Q.popleft()

            for dx, dy in dirs:
                x,y = i+dx, j+dy
                if 0<=x<m and 0<=y<n and not visited[x][y]:
                    res[x][y] = d+1
                    visited[x][y] = True
                    Q.append((x,y,d+1))
                
        return res


