class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        max_longest = 0
        num_set = set(nums)

        for num in num_set:
            if num+1 in num_set: # not a run start
                continue
            longest = 1
            while num -1 in num_set:
                longest += 1
                num -= 1
            max_longest = max(max_longest, longest)        
        return max_longest

