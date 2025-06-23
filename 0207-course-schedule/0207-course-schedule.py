from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False for _ in range(numCourses)]
        path_visited = [False for _ in range(numCourses)]

        adj = defaultdict(list)
        for a,b in prerequisites:
            adj[b].append(a)


        def dfs(node):
            visited[node] = True
            path_visited[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor): 
                        return True
                    path_visited[neighbor] = False
                elif visited[neighbor] and path_visited[neighbor]:
                    return True
            path_visited[node] = False

            return False
                    

        for start in range(numCourses):
            if not visited[start]:
                if dfs(start):
                    return False
                path_visited[start] =False
        return True
        
        