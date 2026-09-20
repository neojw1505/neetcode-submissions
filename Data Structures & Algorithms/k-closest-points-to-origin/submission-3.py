class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max-heap 
        max_heap = []
        for i, (x,y) in enumerate(points):
            dist = (x**2 + y**2)**0.5
            points[i] = [-dist, [x,y]] # negate dist
            heapq.heappush(max_heap, points[i])
            if len(max_heap) > k:
                heapq.heappop(max_heap) # kick largest out, remaining kth closest
        
        return [[x,y] for dist,[x,y] in max_heap]
        

        