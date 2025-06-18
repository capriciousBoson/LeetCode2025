class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums)/2
        if not target.is_integer():
            return False
        target = int(target)

        dp = [[False for _ in range(target+1)] for __ in range(n)]
        for i in range(n):
            dp[i][0] = True

        if nums[0] <= target:
            dp[0][nums[0]] = True
        
        for i in range(1,n):
            for x in range(target+1):
                take = False
                if nums[i] <= x:
                    take = dp[i-1][x-nums[i]]
                not_take = dp[i-1][x]

                dp[i][x] = take or not_take

        return dp[n-1][target]


        # memo = {}
        # def dfs(i,x):
        #     if x==0:
        #             return True
        #     if i==n:
        #         return False
                
        #     if (i,x) in memo:
        #         return memo[(i,x)]
            
        #     if x>=nums[i]:
        #         memo[(i,x)] = dfs(i+1, x-nums[i]) or dfs(i+1, x)
        #     else:

        #         memo[(i,x)] = dfs(i+1, x)

            
        #     return memo[(i,x)]

        # return dfs(0,target)