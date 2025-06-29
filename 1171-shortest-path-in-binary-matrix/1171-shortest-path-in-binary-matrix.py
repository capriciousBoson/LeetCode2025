from collections import defaultdict, deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[n-1][n-1] !=0 or grid[0][0] !=0 : return -1
        visited = set()
        distance = [[float('inf') for _ in range(n)] for __ in range(n)]

        dirs = [(0,1),(1,0), (1,1), (-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]

        Q = deque()
        Q.append([0,0,1])
        visited.add((0,0))
        while Q:
            # Q = deque(sorted(Q,key=lambda x: x[2]))
            x,y, d = Q.popleft()
            if (x,y) == (n-1, n-1) : return d
            if d<distance[x][y] : 
                distance[x][y]  = d

                for dx, dy in dirs:
                    x2,y2= x+dx, y+dy
                    if 0<=x2<n and 0<=y2<n and (x2, y2) not in visited:
                        if grid[x2][y2]==0 :
                            Q.append([x2,y2, d+1])
                            visited.add((x2,y2))

        print(f"distance : {distance}")
        if (n-1, n-1)not in distance or distance[(n-1, n-1)] == float('inf'): return -1

        return distance[(n-1, n-1)]
                
            





        