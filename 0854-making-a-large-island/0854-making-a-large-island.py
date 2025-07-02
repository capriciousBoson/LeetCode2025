from copy import deepcopy
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zero_exists = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    zero_exists = True
        if not zero_exists: return n*n
        
        def findParent(x):
            if parent[x] != x:
                parent[x] = findParent(parent[x])
            return parent[x]

        def unionBySize(u,v):
            root_u = findParent(u)
            root_v = findParent(v)

            if root_u==root_v: return
            if size[root_v] < size[root_u]:
                parent[root_v] = root_u
                size[root_u] += size[root_v]
            else:
                parent[root_u] = root_v
                size[root_v] += size[root_u]
 
        parent = [i for i in range(n*n)]
        size = [1 for i in range(n*n)]
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    for dx, dy in dirs:
                        x,y = i+dx, j+dy
                        if 0<=x<n and 0<=y<n and grid[x][y]==1:
                            a = i*n+j
                            b = x*n + y
                            unionBySize(a,b)

        res = max(size)



        print(f"initial sizes  :{size}")

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:

                    ns = 0 #neighbours sizes sum
                    visited = set()
                    for dx, dy in dirs:
                        x,y = i+dx, j+dy
                        
                        if 0<=x<n and 0<=y<n and grid[x][y]==1:
                                ngh = x*n+y
                                root_ngh = findParent(ngh)
                                if root_ngh not in visited:
                                    ns += size[root_ngh]
                                    visited.add(root_ngh)
                    # print(f"on grid[{i,j}] : {grid[i][j]} - connected neighbours = {ns}")
                    res = max(res, ns+1)
                        


        return res

