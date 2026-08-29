class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_map = collections.defaultdict(int)
        prefix_map[0] = 1
        count = 0
        for n in nums:
            prefix_sum += n
            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum-k]
            prefix_map[prefix_sum] += 1
        return count