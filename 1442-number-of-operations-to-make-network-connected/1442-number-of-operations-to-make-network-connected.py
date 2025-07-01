class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        num_edges = len(connections)
        if num_edges<n-1: return -1
        
        parent = [i for i in range(n)]
        rank = [0 for  _ in range(n)]

        def find(x):
            if parent[x] !=x:
                parent[x] = find(parent[x])
            return parent[x]

        def unionbyrank(a,b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b: return

            if rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
            elif rank[root_a] > rank[root_b]:
                parent[root_b] = parent[root_a]
            else:

                parent[root_b] = root_a
                rank[root_a] += 1

        for u,v in connections:
            unionbyrank(u,v)
        
        connected_components = set()
        for i in range(n):
            connected_components.add(find(i))
        

        return len(connected_components) -1
        