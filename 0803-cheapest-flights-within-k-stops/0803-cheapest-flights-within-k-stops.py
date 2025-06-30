from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = defaultdict(list)
        for src_, dst_, price in flights:
            adj[src_].append((dst_, price))
        
        prices = [float('inf') for _ in range(n)]

        pq = [(0,(src, 0))]
        stops_to = [float('inf') for _ in range(n)]

        while pq:
            price, (city, stops) = heapq.heappop(pq)
            if city==dst and stops<=k+1:
                return price
            if stops>k : continue
            for ngh, price_ in adj[city]:
                if price + price_ < prices[ngh] or stops<stops_to[ngh]:
                    heapq.heappush(pq,(price+price_, (ngh, stops+1)))
                    prices[ngh] = price + price_
                    stops_to[ngh] = stops
        return -1


        