import heapq
from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq map 
        m = Counter(nums)
        # convert into list of tuples (freq, num)
        tuple_list = []
        for key, val in m.items():
            tuple_list.append((val*-1, key)) # freq, num
        # make into a heap -> will look at tuple[0]
        heapq.heapify(tuple_list)
        # get the k max element, but its negative
        # remember multiply -1 later
        res = []
        while len(res) != k:
            f, n = heapq.heappop(tuple_list)
            res.append(n)
        
        return res



