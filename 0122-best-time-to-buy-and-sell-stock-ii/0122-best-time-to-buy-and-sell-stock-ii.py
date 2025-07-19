class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        dp = [[0,0] for __ in range(n+1)]

        for i in range(n-1, -1, -1):
            for can_buy in range(2):
                if can_buy:
                    dp[i][can_buy] =  max( -prices[i] + dp[i+1][0], dp[i+1][1] )
                if not can_buy:
                    dp[i][can_buy] =  max( prices[i] + dp[i+1][1], dp[i+1][0] )

        return dp[0][1]  


        
        ########################################
        ####         MEMOIZATION I          ####
        ########################################
        n = len(prices)
        memo = {}
        def dfs(i, can_buy):
            if i>=n:
                return 0
            if (i, can_buy) not in memo: 
                if can_buy:
                    memo[(i, can_buy)] = max( 
                                                -prices[i] + dfs(i+1, False),
                                                dfs(i+1, True)
                                                )

                if not can_buy:
                    memo[(i, can_buy)] = max(   
                                                prices[i] + dfs(i+1, True),
                                                dfs(i+1, False)
                                                )
                            
                            
            return memo[(i, can_buy)]

        return dfs(0, True)


        ########################################
        ####         MEMOIZATION II         ####
        ########################################

        # n = len(prices)

        # memo = {}

        # def dfs(i, j):
        #     # print(f"\n buy-{i} sell-{j} ---------------")
        #     if i>=n or j>=n: 
        #         return 0
        #     if i>= j: 
        #         return dfs(i, j+1)
        #     if prices[i] >= prices[j]:
        #         return dfs(i+1, j)
        #     if (i,j) not in memo:
        #         buy_and_sell = prices[j] - prices[i] + dfs(j, j+1)
        #         buy_dont_sell = dfs(i, j+1)
        #         dont_buy = dfs(i+1, j)

        #         # print(f"buy and sell at {prices[i],prices[j]}  : {buy_and_sell}")
        #         # print(f"buy dont sell at {prices[i],prices[j]}   : {buy_dont_sell}")
        #         # print(f"dont buy at {prices[i],prices[j]}  : {dont_buy}")

        #         memo[(i,j)] = max(buy_and_sell, buy_dont_sell, dont_buy)

        #     # print(f"max profit for {prices[i],prices[j]} = {memo[(i,j)]}")
        #     return memo[(i,j)]

        # return dfs(0,0)





