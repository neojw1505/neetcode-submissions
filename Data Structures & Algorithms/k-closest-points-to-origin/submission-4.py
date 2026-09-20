class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 📏 Calculate squared distance from origin: x^2 + y^2
        def get_dist(p: List[int]) -> int:
            return p[0]**2 + p[1]**2

        
        def quickSelectHelper(left: int, right: int):
            # 🛑 Base Case: If our partition walls cross or meet, stop immediately!
            if left >= right:
                return
            pivot_dist = get_dist(points[right])
            i = left
            # 🔍 Scan from left up to right - 1 using pointer 'j'
            for j in range(left, right):
                # Check if the current point's distance is strictly smaller than the pivot
                if get_dist(points[j]) < pivot_dist:
                    # If yes, swap it forward to our smaller pile at index 'i'
                    points[i], points[j] = points[j], points[i]
                    i += 1  # Expand the wall forward!
            # 🏁 Swap the pivot from the right wall down onto its final landing pad index 'i'
            points[i], points[right] = points[right], points[i]
            # 🚦 Traffic Cop: If the pivot landed exactly at index k, we are done!
            if i == k:
                return
            elif i > k:
                # The target boundary is in the left pile. Throw right pile in the trash!
                quickSelectHelper(left, i - 1)
            else:
                # The target boundary is in the right pile. Throw left pile in the trash!
                quickSelectHelper(i + 1, right)

        # 🚀 Launch the selector engine across the full outer walls of the array
        quickSelectHelper(0, len(points) - 1)
        # 🏆 Return the first K coordinates from the partitioned array
        return points[:k]