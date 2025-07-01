class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        #using bellman ford algo.
        edges_  = []
        for u,v,w in edges:
            edges_.append([u,v,w])
            edges_.append([v,u,w])

        distances = [[float('inf') for _ in range(n)] for __ in range(n)]
       
        for u, v, w in edges_:
            distances[u][v] = w

        for i in range(n):
            distances[i][i] = 0

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if distances[i][via] != float('inf') and distances[via][j]!=float('inf'):
                        distances[i][j] = min(
                                                distances[i][j],
                                                distances[i][via]+distances[via][j]
                                            )
        
        counts = defaultdict(list)
        for i in range(n):
            counts_i = 0
            for j in range(n):
                if distances[i][j] <= distanceThreshold:
                    counts_i +=1
            counts[counts_i].append(i)
        
        min_connection_cities = counts[min(counts.keys())]

        return max(min_connection_cities)
        


        


       
        


        