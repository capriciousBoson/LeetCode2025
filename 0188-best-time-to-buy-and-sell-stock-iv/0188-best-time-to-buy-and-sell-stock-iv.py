class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2*k+1)] for __ in range(n+1)]

        for i in range(n-1, -1, -1):
            for c in range(2*k):
                if c %2==0:
                    dp[i][c] = max(-prices[i] + dp[i+1][c+1], dp[i+1][c])
                else:
                    dp[i][c] = max(prices[i] + dp[i+1][c+1], dp[i+1][c])
        return dp[0][0]