from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time_taken = [float('inf') for _ in range(n+1)]
        adj = defaultdict(list)

        for u,v,w in times:
            adj[u].append((v,w))
        
        # print(f"adjacency list : {adj}")
        pq = [(0,k)]
        time_taken[k] = 0

        

        while pq:
            time, node = heapq.heappop(pq)

            for ngh, time_ in adj[node]:
                if time+time_ < time_taken[ngh]:
                    heapq.heappush(pq, (time+time_, ngh))
                    time_taken[ngh] = time+time_

        # print(f"timetaken : {time_taken}")
        res = max(time_taken[1:])
        if res == float('inf'): return -1
        return res        