from functools import lru_cache
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        # Memoization Method -------------------------------
        # memo={}
        # @lru_cache(maxsize=None)
        # def dfs(row,col):
        #     if row==n-1:
        #         return matrix[row][col]
            
        #     # down = float('inf')
        #     # left = float('inf')
        #     # right = float('inf')

        #     down = dfs(row+1,col)
        #     left = dfs(row+1,col-1) if col> 0 else float('inf')
        #     right = dfs(row+1,col+1)if col<n-1 else float('inf')
            
        #     return matrix[row][col] + min(left,down,right)
        # return min(dfs(0,i) for i in range(n))
        
        # Tabulation method ----------------------------------------
        rows , cols = len(matrix), len(matrix[0])


        dp = [[0  for _ in range(cols)] for _ in range(rows)]
        for i in range(cols):
            dp[0][i] = matrix[0][i]
        
        for i in range(rows):
            for j in range(cols):
                if i==0: continue
                left = float('inf')
                right = float('inf')
                if j>0: left = dp[i-1][j-1]
                if j<cols-1: right = dp[i-1][j+1]
                down = dp[i-1][j]
                dp[i][j] = matrix[i][j] + min(left, down, right)

        return min(dp[-1])

                
        