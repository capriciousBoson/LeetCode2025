class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        n = len(coins)
        
        def dfs(x, i):
            
            if x==amount:
                return  1

            elif x > amount:
                return 0

            if i==n : return 0

            if (x,i) not in memo:
                memo[(x,i)] = dfs(x+coins[i], i ) + dfs(x, i+1)
            return memo[(x,i)]


        return dfs(0, 0)

        