from collections import defaultdict, deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        adj = defaultdict(list)
        indegrees = [0 for _ in range(n)]

        # reverse graph adjacency list
        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegrees[i] += 1
        
        Q = deque()
        for i in range(n):
            if indegrees[i]==0:
                Q.append(i)

        res = []
        while Q:
            current = Q.popleft()
            res.append(current)

            for neighbor in adj[current]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    Q.append(neighbor)

        return sorted(res)



        