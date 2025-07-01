class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        max_row = 0
        max_col = 0

        for i, j in stones:
            max_row = max(max_row, i)
            max_col = max(max_col, j)

        parent = [i for i in range(max_row + max_col +2)]
        size = [1 for _ in range(max_row + max_col +2)]
        
        def findParent(x):
            if x!=parent[x]:
                parent[x] = findParent(parent[x])
            return parent[x]

        def unionBySize(u,v):
            root_u = findParent(u)
            root_v = findParent(v)

            if root_u==root_v: return
            if size[root_u] > size[root_v]:
                parent[root_v] = root_u
                size[root_u] += size[root_v]
            else:
                parent[root_u] = root_v
                size[root_v] += size[root_u]
        

        stoneNodes = []
        for i,j in stones:
            u = i
            v = j+ max_row + 1
            unionBySize(u,v)
            stoneNodes.append((u,v))


        components = set()
        for i,j in stoneNodes:
            components.add(findParent(i))

        connected_components = len(components)
        
        
        return n - connected_components