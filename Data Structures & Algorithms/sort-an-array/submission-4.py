class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # heap sort T:O(nlogn) S:O(n)
        heapq.heapify(nums)
        res = []
        while nums:
            res.append(heapq.heappop(nums))
        return res