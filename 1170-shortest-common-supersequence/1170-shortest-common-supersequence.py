class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        res = ""

        p,q = m,n
        while p>0 and q>0:
            if str1[p-1] == str2[q-1]:
                res = str1[p-1]+res

                p = p-1
                q = q-1
            else:
                if dp[p-1][q] > dp[p][q-1]:
                    res = str1[p-1]+res
                    p = p-1
                else:
                    res = str2[q-1]+res
                    q= q-1
        while p>0:
            res = str1[p-1]+res
            p -= 1
        
        while q>0:
            res = str2[q-1]+res
            q -= 1

        
        return res
        