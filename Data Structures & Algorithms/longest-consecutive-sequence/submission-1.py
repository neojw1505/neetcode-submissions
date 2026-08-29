from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # store every num in hashmap for O(1) access
        map = Counter(nums)
        # iterate nums and -1 while keeping track of length
        i, maxLength = 0,0
        for n in nums:
            length = 1
            # check if n - 1 is in map, length += 1
            while n - 1 in map:
                length += 1
                n -= 1
            # compare length with maxLenght
            maxLength = max(maxLength, length)
        return maxLength
