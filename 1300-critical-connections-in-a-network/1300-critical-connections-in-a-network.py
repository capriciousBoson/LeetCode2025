class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        if len(connections) <3:
            return connections
        adj = collections.defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)

        time = [0 for _ in range(n)]
        low = [0 for _ in range(n)]
        # visited = [False for _ in range(n)]
        bridges = []

        timer = -1
        def dfs(node, parent_node):
            nonlocal timer
            timer += 1
            time[node] = timer
            low[node] = timer
            # visited[node] = True
            
            for ngh in adj[node]:
                if ngh==parent_node: continue
                
                if not time[ngh] :
                    dfs(ngh, node)
                    low[node] = min(low[node], low[ngh])
                    if time[node] < low[ngh]:
                        bridges.append([node, ngh])
                # if time[ngh]:
                low[node] = min(low[node], low[ngh])


        dfs(0,-1)


        return bridges
