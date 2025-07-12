class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(n+1)] for __ in range(amount  +1)]
        for amt in range(amount+1):
            dp[amt][n] = 0
        dp[0][n]=1


        for amt  in range(amount+1):
            for i in range(n-1, -1, -1):
                dp[amt][i] = dp[amt][i+1]
                if amt-coins[i] >=0:
                    dp[amt][i] += dp[amt-coins[i]][i]
        return dp[amount][0]
        # memo = {}

        # def dfs(x, i):
            
        #     if x==amount:
        #         return  1

        #     elif x > amount:
        #         return 0

        #     if i==n : return 0

        #     if (x,i) not in memo:
        #         memo[(x,i)] = dfs(x+coins[i], i ) + dfs(x, i+1)
        #     return memo[(x,i)]


        # return dfs(0, 0)
 
        