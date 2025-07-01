class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        num_edges = len(connections)
        if num_edges<n-1: return -1
        
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] !=x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a,b):
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                parent[root_b] = root_a
        for u,v in connections:
            union(u,v)
        
        connected_components = set()
        for i in range(n):
            connected_components.add(find(i))
        
        
        
        return len(connected_components) -1
        