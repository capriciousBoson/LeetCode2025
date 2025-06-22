class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        x  = n%k
        print(f"n : {n}, remainderv: {x}")
        res = []
        a = 0
        for i in range(k,n+k-x,k):
            print(f"s[{a}:{i}] = {s[a:i]}")
            res.append(s[a:i])
            a += k 
        print(res)
        if x:
            res.append(s[-x:]+fill*(k-x))
        return res


        