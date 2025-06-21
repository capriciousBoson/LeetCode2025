from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n  = len(image), len(image[0])
        Q = deque()
        Q.append((sr,sc))

        og = image[sr][sc]
        
        if og == color: return image
        image[sr][sc] = color

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        while Q:
            i, j = Q.popleft()
            

            for dx, dy in dirs:
                x,y = i+dx, j+dy
                if 0<=x<m and 0<=y<n and image[x][y] == og:
                    image[x][y] = color
                    Q.append((x,y))
        return image


        