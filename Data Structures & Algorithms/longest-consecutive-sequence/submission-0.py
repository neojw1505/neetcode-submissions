class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        s = set(nums)
        for n in nums:
            # find start of seq
            if n - 1 not in s:
                # check n + 1 inside, if yes increase the cur length
                length = 1
                while n + 1 in s:
                    length += 1
                    n += 1
                # compare length with maxLength
                maxLength = max(maxLength, length)
        return maxLength