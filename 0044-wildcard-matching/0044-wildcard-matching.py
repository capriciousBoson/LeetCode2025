class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[False for _  in range(n+1)] for __ in range(m+1)]

        dp[0][0] = True
        for j in range(n+1):
            x = True
            for c in p[0:j]:
                if c !="*":
                    x =False
            dp[0][j] = x
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
            
                elif p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = False
        # for row in dp: print(row)

        return dp[m][n]
