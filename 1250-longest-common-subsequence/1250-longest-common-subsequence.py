class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}
        def dfs(i1, i2):
            if i1 < 0 or i2<0:
                return 0
            if (i1, i2) not in memo:
                if text1[i1] == text2[i2]:
                    memo[(i1, i2)] = 1 + dfs(i1-1, i2-1)
                else:
                    memo[(i1, i2)] = max(dfs(i1-1, i2), dfs(i1, i2-1))
            return memo[(i1, i2)]

        return dfs(len(text1)-1, len(text2)-1)
        