from itertools import combinations
from collections import defaultdict
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        def subsetSum(arr):
            k = len(arr)
            res = defaultdict(list)
            for size in range(k + 1):
                for comb in combinations(arr, size):
                    res[size].append(sum(comb))
            return res

        n = len(nums)//2
        total = sum(nums)//2
        left_sums = subsetSum(nums[:n])
        right_sums = subsetSum(nums[n:])

        ans = float('inf')

        total_sum  = sum(nums)
        for x in range(n+1):
            right_list = sorted(right_sums[n - x])
            for ls in left_sums[x]:
                target = total - ls
                
                
                idx = bisect.bisect_left(right_list, target)

                for j in [idx, idx-1]:
                    if 0 <= j < len(right_list):
                        rs = right_list[j]
                        total_half_sum = ls+rs
                        diff = abs(total_sum-2*total_half_sum)
                        ans = min(ans,diff)
        return ans






            

            



        