class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        src_to_dst_and_weight = collections.defaultdict(list)

        for u,v,w in edges:
            src_to_dst_and_weight[u].append((w,v))

        min_heap = [(0,src)]
        visited = set()
        res = {}

        while min_heap:
            weight, dst = heapq.heappop(min_heap)

            if dst in visited: # already found shortest distance for vertex
                continue 

            visited.add(dst) # if not add to the vertex
            res[dst] = weight

            # add vertex neighbors 
            for w1, d1 in src_to_dst_and_weight[dst]:
                 if d1 not in visited:
                    heapq.heappush(min_heap, (weight + w1, d1))

        for i in range(n):
            if i not in res:
                res[i] = -1
                
        return res


            


        