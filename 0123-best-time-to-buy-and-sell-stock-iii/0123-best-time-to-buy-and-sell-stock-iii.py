class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        memo = {}

        def dfs(i, c):
            if i >= n or c>=4:
                return 0
            if (i,c) not in memo:
                

                if c in (0,2):
                    memo[(i,c)] = max(-prices[i]+dfs(i+1, c+1), dfs(i+1,c))
                if c in (1,3):
                    memo[(i,c)] =  max(prices[i] + dfs(i+1, c+1), dfs(i+1,c))
            return memo[(i,c)]
        return dfs(0,0)




        