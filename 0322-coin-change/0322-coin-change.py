class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        s = len(coins)

        memo = {}

        def dfs(i, money):
        
            if money == amount:
                return 0
            if money > amount or i==s:
                return float('inf')

            if (i, money) in memo: return memo[(i,money)]
            take_and_keep = 1 + dfs(i, money + coins[i])
            take_and_move = 1 + dfs(i+1, money + coins[i])
            not_take = dfs(i+1, money)

            memo[(i,money)] = min(take_and_keep,take_and_move, not_take )

            return  memo[(i,money)]
        
        n = dfs(0,0)
        if n==float('inf'): return -1
        return n

            
        