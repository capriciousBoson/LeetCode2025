class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # we have to convert word1 to word2
        m,n = len(word1), len(word2)

        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        
        for i in range(1,m+1): # source word loop/pointer
            for j in range(1,n+1):  # target word loop/pointer
                if word1[i-1] != word2[j-1] : 

                    # we insert to the right of  index 'i' in word1,
                    insert = dp[i][j-1] 

                    # we delete current index i in word1
                    delete = dp[i-1][j]

                    replace = dp[i-1][j-1]

                    dp[i][j] = 1+ min(insert, delete, replace)
                else:
                    dp[i][j] = dp[i-1][j-1]

        for row in dp: print(row)

        return dp[m][n]

                    






        # def dfs(i, j):
        #     # if we have exhausted all chracters of target,
        #     # then we need to insert all remaining characters of source
        #     # as there are no chracters left to replace or delete
        #     # in the target

        #     if i<0:
        #         return j+1 
            
        #     # if we have exhausted all characters of source,
        #     # then we need to delete all the remainign characters of the target
        #     # as there are no chracters left in the source that 
        #     # need to be matched in the target

        #     if j<0:
        #         return i+1
            
        #     if word1[]
        