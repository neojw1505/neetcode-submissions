class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i, (x,y) in enumerate(points):
            dist = x**2 + y**2
            points[i] = [dist, (x,y)]
        self.quickSelect(points,0,len(points)-1,k)
        return [item1 for dist, item1 in points[:k]]

    def quickSelect(self, points, left, right, k):
        # base 
        if left >= right:
            return
        # define pivot
        pivot = points[right]
        i = left
        for j in range(left, right):
            if points[j][0] < points[right][0]:
                points[i], points[j] = points[j], points[i]
                i += 1
        # swap pivot to correct separation point
        points[right], points[i] = points[i], points[right]
        # found k closest points
        if i == k:
            return 
        elif i > k: # k in left pile 
            self.quickSelect(points, left, i-1, k) # search left pile
        else:
            self.quickSelect(points, i+1, right, k) # search right pile

