class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        Q = []
        Q.append((grid[0][0],0,0))
        res = -float('inf')
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = [[False for _ in range(n)] for __ in range(n)]
        reached = False

        while Q:
            elevation, i,j = heapq.heappop(Q)
            res = max(res, elevation)
            visited[i][j] = True

            if i==n-1 and j==n-1: return res

            for dx, dy in dirs:
                x,y = i+dx, j+dy
                if 0<=x<n and 0<=y<n and not visited[x][y]:
                    heapq.heappush(Q,(grid[x][y], x, y))



        return res



        