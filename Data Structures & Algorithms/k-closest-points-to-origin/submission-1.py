class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i, (x,y) in enumerate(points):
            dist = (x**2 + y**2)**0.5
            points[i] = [dist, [x,y]]
        heapq.heapify(points)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(points)[1])
        
        return res
        
        