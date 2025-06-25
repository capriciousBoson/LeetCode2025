from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [False for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        adj = defaultdict(list)
        res = []
        for a,b in prerequisites:
            adj[b].append(a)
            indegrees[a] +=1
        


        
        Q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                Q.append(i)
        while Q:
            current = Q.popleft()
            res.append(current)
            for node in adj[current]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    Q.append(node)

        if len(res)==numCourses:
            return res

        return []
        