class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1 for i in range(n)]
        path = [i for i in range(n)]
        res = 0
        res_idx = 0

        for i in range(n):
            for prev in range(i):
                if nums[i]%nums[prev]==0 :
                    # dp[i] = max(dp[i], 1+dp[prev])
                    if dp[i] < 1+dp[prev]:
                        dp[i] = 1+dp[prev]
                        path[i] = prev
            if dp[i]>res:
                res = dp[i]
                res_idx = i
        
        ans = [nums[res_idx]]
        j = res_idx
        while True:
            if path[j]==j: break
            else:
                ans.append(nums[path[j]])
                j = path[j]
        return ans[::-1]
        
            
            

        