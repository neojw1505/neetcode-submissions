class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_num = collections.Counter(nums)
        max_heap = [(-val,key) for key,val in freq_num.items()]
        heapq.heapify(max_heap) # O(n)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res
