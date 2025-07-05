class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ns = len(s)
        ng = len(g)
        if ns==0 or ng==0: return 0

        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)
        # g.sort()
        # s.sort()

        g_p = 0
        s_p = 0
        

        res = 0 
        while g_p < ng and s_p < ns:
            print(f"current greed = {g[g_p]} , cookie size : {s[s_p]}")
            if s[s_p] >= g[g_p]:
                res += 1
                s_p += 1
                g_p += 1
                # print(f"updated satisfied to :  {res}")
            elif s[s_p] < g[g_p]:
                g_p +=1
        
        return res
  