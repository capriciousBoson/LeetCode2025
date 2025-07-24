class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[0 for _ in range(n+1)] for __ in range(n+1)]

        for i in range(n-1, -1, -1):
            for prev in range(i-1, -2, -1):
                if prev==-1 or nums[i] > nums[prev]  :
                    dp[i][prev+1] = max(1+dp[i+1][i+1], dp[i+1][prev+1])
                else:
                    dp[i][prev+1] = dp[i+1][prev+1]
        return dp[0][0]



        # memo = {}

        # def dfs(prev_idx, i):
        #     if i>= n :
        #         return 0
        #     if (prev_idx, i) not in memo:
        #         if prev_idx==-1 or nums[i]>nums[prev_idx]:
        #             memo[(prev_idx,i)] =  max(1+dfs(i, i+1) , dfs(prev_idx, i+1))
        #         else:
        #             memo[(prev_idx,i)] =  dfs(prev_idx, i+1)
        #     return memo[(prev_idx,i)]
        # return dfs(-1, 0)
        