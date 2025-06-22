from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [False for _ in range(n)]

        colors = [0 for _ in range(n)]

        for start in range(n):
            if not visited[start]:
                visited[start] = True
                colors[start] = 1
                Q = deque()
                Q.append((-1, start, colors[start]))

                while Q:
                    parent, current, current_color = Q.popleft()

                    for neighbor in graph[current]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            colors[neighbor] = 1 if current_color ==2 else 2
                            Q.append((current, neighbor, colors[neighbor]))
                        elif visited[neighbor] and neighbor!=parent:
                            if colors[neighbor] == current_color:
                                return False
        
        return True


        