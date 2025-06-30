from collections import defaultdict
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        times = [float('inf') for _ in range(n)]
        times[0] = 0
        counts = [0 for _ in range(n)]
        counts[0] = 1
        adj = defaultdict(list)

        for u,v,t in roads:
            adj[u].append((v,t))
            adj[v].append((u,t))
        
        MOD = 10**9 + 7
        pq = [(0,0)]
        while pq:
            time, node = heapq.heappop(pq)
            if time > times[node]: 
                continue
            for ngh, time_ in adj[node]:
                if time+time_ < times[ngh]:
                    heapq.heappush(pq,(time+time_, ngh))
                    times[ngh] = time+time_
                    counts[ngh] = counts[node]
                elif time+time_ == times[ngh]:
                    counts[ngh] +=counts[node]
        
        return counts[n-1]%MOD
        