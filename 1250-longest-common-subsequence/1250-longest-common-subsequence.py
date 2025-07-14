class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m,n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for j in range(m+1)]

        # for i in range(m+1):
        #     dp[i][0] = 0
        # for j in range(n+1):
        #     dp[0][j] = 0

        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]



        # memo = {}
        # def dfs(i1, i2):
        #     if i1 < 0 or i2<0:
        #         return 0
        #     if (i1, i2) not in memo:
        #         if text1[i1] == text2[i2]:
        #             memo[(i1, i2)] = 1 + dfs(i1-1, i2-1)
        #         else:
        #             memo[(i1, i2)] = max(dfs(i1-1, i2), dfs(i1, i2-1))
        #     return memo[(i1, i2)]

        # return dfs(len(text1)-1, len(text2)-1)
        