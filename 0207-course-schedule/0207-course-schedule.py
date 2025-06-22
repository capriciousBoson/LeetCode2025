from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False for _ in range(numCourses)]
        path_visited = [False for _ in range(numCourses)]

        adj = defaultdict(list)
        for a,b in prerequisites:
            adj[b].append(a)


        def dfs(node):
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    path_visited[neighbor] = True
                    if dfs(neighbor): return True
                    path_visited[neighbor] = False
                elif visited[neighbor] and path_visited[neighbor]:
                    return True
            return False
                    

        for start in range(numCourses):
            if not visited[start]:
                visited[start] = True
                path_visited[start] = True
                if dfs(start):
                    return False
                path_visited[start] =False
        return True
        
        