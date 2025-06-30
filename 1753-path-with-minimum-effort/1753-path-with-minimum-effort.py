from collections import defaultdict, deque
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        res = float('inf')
        rows = len(heights)
        cols = len(heights[0])


        efforts = [[float('inf') for _ in range(cols)] for _ in range(rows)]

        dirs = [(1,0),(0,1),(-1,0), (0,-1)]

        pq = [(0,(0,0))]
        
        while pq:
            
            effort,(x,y) = heapq.heappop(pq)
            efforts[x][y] = min(efforts[x][y], effort)
            for dx, dy in dirs:
                x2,y2 = x+dx, y+dy
                if 0<=x2<rows and 0<=y2<cols:
                    effort2 = max(effort, abs(heights[x][y] - heights[x2][y2]))
                    # Q.append((x2,y2,effort2))
                    if efforts[x2][y2] > effort2 : 
                        efforts[x2][y2] = effort2
                        heapq.heappush(pq,(effort2,(x2,y2)))

        return efforts[rows-1][cols-1]           
        