class Solution:
    def minInsertions(self, s: str) -> int:

        n = len(s)
        dp = [[0 for _ in range(n)] for __ in range(n)]

        # for i in range(n):
        #     dp[i][i] = 0

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 1 + min(
                                            dp[i+1][j],
                                            dp[i][j-1]
        
                                        )
        return dp[0][n-1]


        # MEMOIZATION BASED SOLUTION --------------

        # n = len(s)
        # memo = {}
        # def util(start, end):
        #     if start >= end :
        #         return 0
        #     if (start,end) not in memo :

        #         if s[start]==s[end]:
        #             memo[(start, end)] = util(start+1, end-1)
        #         else:
        #             memo[(start, end)] = 1 + min(
        #                                             util(start+1, end), 
        #                                             util(start, end-1)
        #                                             )
        #     return memo[(start, end)] 
        # return util(0,n-1)