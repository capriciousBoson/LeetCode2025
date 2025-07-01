from collections import defaultdict
from itertools import combinations
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        
        def findParent(x):
            print(f"searching for parent of x : {x}")
            if x!=parent[x]:
                parent[x] = findParent(parent[x])
            return parent[x]

        def union(u,v):
            root_u = findParent(u)
            root_v = findParent(v)

            if root_u==root_v: return
            parent[root_u] = root_v
        
        # build the ds

        emails = []
        names = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                parent[email] = email
                emails.append(email)
                names[email] = name

        for account in accounts:
            name = account[0]
            for e1, e2 in combinations(account[1:], 2):
                union(e1, e2)
        
        groups = defaultdict(set)
        for email in emails:
            root_email = findParent(email)
            groups[root_email].add(email)
        
        res = []
        for key, _ in groups.items():
            name = names[key]
            groups[key] = [name] + sorted(groups[key])
            res.append(groups[key])
        return res
        
        

                
        



               


        