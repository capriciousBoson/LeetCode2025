from collections import defaultdict, deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[n-1][n-1] !=0: return -1

        adj = defaultdict(list)
        distance = defaultdict(int)

        dirs = [(0,1),(1,0), (1,1), (-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]
        # visited = [[False for _ in range(n)] for __ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] ==0:
                    distance[i*n+j] = float('inf')
                    for dx, dy in dirs:
                        x,y = i+dx, j+dy
                        if 0<=x<n and 0<=y<n:
                            if grid[x][y]==0 : 
                                adj[i*n+j].append(x*n+y)
        Q = deque()
        Q.append([0,1])
        while Q:
            node, d = Q.popleft()
            if d<distance[node] : 
                distance[node]  = d

                for ngh in adj[node]:
                    
                    Q.append([ngh, d+1])


        if distance[n**2-1] == float('inf'): return -1

        return distance[n**2-1]
                
            





        