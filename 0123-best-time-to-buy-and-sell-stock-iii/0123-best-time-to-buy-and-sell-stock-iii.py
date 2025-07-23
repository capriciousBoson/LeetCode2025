class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(5)] for __  in range(n+1)]

        for i in range(n-1, -1, -1):
            for c in range(4):
                if c in (0,2):
                    dp[i][c] = max(-prices[i]+dp[i+1][c+1], dp[i+1][c])
                if c in (1,3):
                    dp[i][c] = max(+prices[i]+dp[i+1][c+1], dp[i+1][c])


        return dp[0][0]


        # memo = {}

        # def dfs(i, c):
        #     if i >= n or c>=4:
        #         return 0
        #     if (i,c) not in memo:
                

        #         if c in (0,2):
        #             memo[(i,c)] = max(-prices[i]+dfs(i+1, c+1), dfs(i+1,c))
        #         if c in (1,3):
        #             memo[(i,c)] =  max(prices[i] + dfs(i+1, c+1), dfs(i+1,c))
        #     return memo[(i,c)]
        # return dfs(0,0)




        