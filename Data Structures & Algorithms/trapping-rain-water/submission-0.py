class Solution:
    def trap(self, height: List[int]) -> int:
        # formula: min(left_max,right_max) - height[i]
        left_max = 0
        right_max = 0
        l = 0
        r = len(height)-1
        trapped = 0

        while l <= r:
            # left is bottleneck
            if left_max < right_max:
                water = left_max - height[l]
                if water > 0:
                    trapped += water
                left_max = max(left_max, height[l])
                l += 1
            # right is bottleneck
            else:
                water = right_max - height[r]
                if water > 0:
                    trapped += water
                right_max = max(right_max, height[r])
                r -= 1
        return trapped
                


            