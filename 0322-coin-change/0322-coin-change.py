class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins.sort(reverse = True)
        s = len(coins)

        memo = {}

        def dfs( money):
        
            if money == amount:
                return 0
            if money > amount:
                return float('inf')

            if money in memo: 
                return memo[money]
            
            res = float('inf')
            # take_and_keep = 1 + dfs(i, money + coins[i])
            # take_and_move = 1 + dfs(i+1, money + coins[i])
            # not_take = dfs(i+1, money)

            for coin in coins:
                res =min(res, 1+ dfs(money+coin))

            memo[money] =res

            return  memo[money]
        
        n = dfs(0)
        if n==float('inf'): return -1
        return n

            
        