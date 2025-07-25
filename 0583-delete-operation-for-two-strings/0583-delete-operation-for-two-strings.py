class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # print(f"lcs - {dp[m][n]}")
        res = 0
        if m> dp[m][n]:
            res += m-dp[m][n]
        if n > dp[m][n]:
            res += n-dp[m][n]

        

        return res


        