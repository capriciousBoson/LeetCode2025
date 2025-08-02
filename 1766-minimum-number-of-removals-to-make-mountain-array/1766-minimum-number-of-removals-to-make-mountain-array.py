class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n=len(nums)
        dp1 = [1 for i in range(n)]
        dp2 = [1 for i in range(n)]

        for i in range(n):
            for prev in range(i):
                if nums[i]>nums[prev]:
                    dp1[i] = max(dp1[i], 1+dp1[prev])
                if nums[-i-1] > nums[-prev-1]:
                    dp2[i] = max(dp2[i], 1+dp2[prev])


        lb  = 0
        for i in range(n):
            if dp1[i]>1 and dp2[-i-1] >1:
                lb = max(lb, dp1[i] + dp2[-i-1]-1)
        
        
        return n-lb
