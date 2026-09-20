class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min-heap solution
        for i, (x,y) in enumerate(points): # O(n)
            dist = (x**2 + y**2)**0.5
            points[i] = [dist, [x,y]]
        heapq.heapify(points) # O(n)

        res = []
        for _ in range(k): 
            res.append(heapq.heappop(points)[1]) 
        
        return res
        
    # T: O(klogn)
    # S: O(k) if res counted as extra space
        