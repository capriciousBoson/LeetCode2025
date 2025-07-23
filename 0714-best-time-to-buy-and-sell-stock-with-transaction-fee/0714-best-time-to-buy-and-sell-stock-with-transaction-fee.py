class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0,0] for __ in range(n+1)]

        for i in range(n-1, -1, -1):
            for can_buy in range(2):
                if can_buy:
                    dp[i][can_buy] = max(-prices[i] + dp[i+1][0], dp[i+1][1])
                else:
                    dp[i][can_buy] = max(prices[i]-fee+dp[i+1][1], dp[i+1][0])
        return dp[0][1]
        