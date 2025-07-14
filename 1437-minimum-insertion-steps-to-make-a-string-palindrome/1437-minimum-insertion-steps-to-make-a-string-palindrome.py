class Solution:
    def minInsertions(self, s: str) -> int:
        
        n = len(s)
        memo = {}
        def util(start, end):
            if start >= end :
                return 0
            if (start,end) not in memo :

                if s[start]==s[end]:
                    memo[(start, end)] = util(start+1, end-1)
                else:
                    memo[(start, end)] = 1 + min(
                                                    util(start+1, end), 
                                                    util(start, end-1)
                                                    )
            return memo[(start, end)] 
        return util(0,n-1)