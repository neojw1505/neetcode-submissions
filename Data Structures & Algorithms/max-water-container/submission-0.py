class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        maxWater = 0 

        while L < R:
            length = R - L
            breadth = min(heights[R], heights[L])
            areaOfWater = length * breadth

            maxWater = max(areaOfWater, maxWater)
            
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        
        return maxWater