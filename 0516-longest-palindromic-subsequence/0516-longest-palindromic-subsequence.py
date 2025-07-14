from copy import deepcopy
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # t = s[::-1]
        n = len(s)
        dp = [[0 for _ in range(n+1)] for __ in range(n+1)]

        # print(f"s : {s}  ||  t : {t}")

        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1] == s[::-1][j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # for row in dp: print(row)
        return dp[n][n]
        