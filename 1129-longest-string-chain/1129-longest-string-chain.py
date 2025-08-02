class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def fun(s1,s2):
            n1, n2 = len(s1), len(s2)
            if n1 +1 != n2:
                return False
            
            i, j = 0, 0
            while i <n1 and j<n2:
                if s1[i]==s2[j]:
                    i += 1
                    j += 1
                else:
                    j +=1
            return i==n1
        words = sorted(words, key = lambda x: len(x))
        print(f"words : {words}")
        n = len(words)
        dp = [1 for i in range(n)]
        res = 0
        for i in range(n):
            for prev in range(i):
                if fun(words[prev], words[i]):
                    print(f"\nmatched : {words[prev], words[i]}")
                    dp[i] = max(dp[i], 1 + dp[prev])
                    print(f"dp[{i}] = {dp[i]}")
            res = max(res, dp[i])
        print(f"dp : {dp}")
        return res
        