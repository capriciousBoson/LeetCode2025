class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums)/2
        if not target.is_integer():
            return False
        target = int(target)
        memo = {}

        def dfs(i,x):
            if x==0:
                    return True
            if i==n:
                return False
                
            if (i,x) in memo:
                return memo[(i,x)]
            
            # if x>target:
            #     memo[(i,x)] = False
            #     return False
            memo[(i,x)] = dfs(i+1, x-nums[i]) or dfs(i+1, x)
            
            return memo[(i,x)]

        return dfs(0,target)