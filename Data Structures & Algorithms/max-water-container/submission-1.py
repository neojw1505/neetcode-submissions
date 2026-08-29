class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l,r = 0, len(heights)-1
        
        while l < r:
            # formula: w * h
            w = r - l
            h = min(heights[l], heights[r])
            maxWater = max(maxWater, w*h)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxWater