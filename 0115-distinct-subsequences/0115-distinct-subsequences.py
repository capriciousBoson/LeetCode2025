class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        memo = {}

        def dfs(i, j):
            if j < 0:
                return 1
            if i<0 :
                return 0

            if (i,j) not in memo:
                if s[i]==t[j]:
                    memo[(i,j)] =  dfs(i-1, j-1) + dfs(i-1, j)
                else:
                     memo[(i,j)] =  dfs(i-1, j)
                     
            return memo[(i,j)]

        return dfs(m-1, n-1)
