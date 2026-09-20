class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        max_longest = 0
        seen = set()
        for i in range(n):
            longest = 0
            j = i
            seen.add(nums[i])
            while j > 0:
                if nums[j]-1 in seen:
                    longest += 1
                j -= 1
            max_longest = max(max_longest, longest)
        
        return max_longest

