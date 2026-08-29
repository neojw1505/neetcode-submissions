class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # create maxHeap
        minHeap = []
        for num in count.keys():
            heapq.heappush(minHeap, (count[num], num)) # heap sorts by first value in tuple
            # keep heap to top k elements 
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        # TC: O(k * log(N))
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res
        


