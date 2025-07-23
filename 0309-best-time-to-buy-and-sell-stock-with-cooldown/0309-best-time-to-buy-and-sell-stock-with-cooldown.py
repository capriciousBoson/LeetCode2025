class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        dp = [[0,0] for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for can_buy in range(2):
                if can_buy:
                    dp[i][can_buy] = max(-prices[i]+dp[i+1][0], dp[i+1][1])
                else:
                    if i+2 <=n-1:
                        dp[i][can_buy] = max(prices[i]+dp[i+2][1], dp[i+1][0])
                    else:
                        dp[i][can_buy] = max(prices[i], dp[i+1][0])
        return dp[0][1]