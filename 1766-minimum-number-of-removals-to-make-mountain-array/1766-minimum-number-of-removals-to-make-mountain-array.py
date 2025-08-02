class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        lis = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)

        lds = [1] * n
        for i in reversed(range(n)):
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], lds[j] + 1)

        max_mountain = 0
        for i in range(1, n-1):
            if lis[i] > 1 and lds[i] > 1:
                mountain_len = lis[i] + lds[i] - 1
                max_mountain = max(max_mountain, mountain_len)

        return n - max_mountain
        # n=len(nums)
        # dp1 = [1 for i in range(n)]
        # dp2 = [1 for i in range(n)]

        # for i in range(n):
        #     for prev in range(i):
        #         if nums[i]>nums[prev]:
        #             dp1[i] = max(dp1[i], 1+dp1[prev])
        #         if nums[-i-1] > nums[-prev-1]:
        #             dp2[i] = max(dp2[i], 1+dp2[prev])


        # lb  = 0
        # for i in range(n):
        #     if dp1[i]==1 or dp2[-i-1]==1: continue
        #     lb = max(lb, dp1[i] + dp2[-i-1]-1)
        
        
        # return n-lb
