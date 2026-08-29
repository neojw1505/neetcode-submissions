class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # index is the freq, values at that index have the freq
        for num, freq in count.items():
            buckets[freq].append(num)
        
        res = []
        # start from the back
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                if len(res) == k:
                    return res
                res.append(num)
        return res
        


