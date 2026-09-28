class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_freq = collections.defaultdict(int)
        counts = 0 
        prefix_sum_freq[0] = 1
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_sum_freq.keys():
                counts += prefix_sum_freq[prefix_sum - k]
            prefix_sum_freq[prefix_sum] += 1
        return counts 
