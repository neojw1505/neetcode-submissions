class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_list = collections.defaultdict(list)
        
        for u,v,w in edges:
            adj_list[u].append((v,w))
        
        visited = set()
        min_heap = [(0,src)]
        shortest = {}

        while min_heap:
            w1,n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue

            visited.add(n1)
            shortest[n1] = w1

            if len(shortest) == n:
                break

            for n2,w2 in adj_list[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap,(w1+w2,n2))
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest


