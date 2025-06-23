from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        adj = defaultdict(list)
        safenodes = [0 for i in range(n)]
       
        visited = [False for _ in range(n)]
        path_visited= [False for __ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj[i].append(node)
            
    
        def dfs(node):
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    path_visited[neighbor] = True
                    if dfs(neighbor):
                        safenodes[neighbor] = 0
                        return True
                    path_visited[neighbor] = False
                elif visited[neighbor] and path_visited[neighbor]:
                    safenodes[neighbor] = 0
                    return True

            safenodes[node] = 1
            return False

        res = []       
        for start in range(n):
            if not visited[start]:
                dfs(start)

        for i in range(n):
            if safenodes[i]:
                res.append(i)

        return res
                
