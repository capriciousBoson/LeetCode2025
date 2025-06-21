class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u,v):
            root_u = find(u)
            root_v = find(v)

            if root_u != root_v:
                parent[root_v] = root_u

        n = len(isConnected)
        parent = {i:i for i in range(n)}
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    union(i,j)
        provinces = set(find(i) for i in range(n))
        return len(provinces)
