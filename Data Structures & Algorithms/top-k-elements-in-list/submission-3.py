class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = collections.Counter(nums)
        maxHeap = [(-freq,num) for num,freq in num_freq.items()]      
        heapq.heapify(maxHeap) # convert to heap 

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(maxHeap)[1])
        return ans
