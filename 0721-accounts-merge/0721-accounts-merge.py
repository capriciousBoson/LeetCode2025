from collections import defaultdict
from itertools import combinations
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        
        def findParent(x):
            # print(f"searching for parent of x : {x}")
            if x!=parent[x]:
                parent[x] = findParent(parent[x])
            return parent[x]

        def union(u,v):
            root_u = findParent(u)
            root_v = findParent(v)

            if root_u==root_v: return
            parent[root_u] = root_v
        
        # build the ds

        emails = set()
        names = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                parent[email] = email
                emails.add(email)
                names[email] = name

        for account in accounts:
            for email in account[2:]:
                union(account[1], email)
        
        groups = defaultdict(set)
        for email in emails:
            root_email = findParent(email)
            groups[root_email].add(email)
        
        res = []
        for key in groups:
            res.append( [names[key]] + sorted(groups[key]))

        return res
        
        

                
        



               


        