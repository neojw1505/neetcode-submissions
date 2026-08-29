class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLongest = 0
        for num in numSet:
            if num - 1 not in numSet: # start of a sequence
                longest = 1
                while num+1 in numSet: # if 
                    longest += 1
                    num += 1
                maxLongest = max(maxLongest, longest)
        return maxLongest 

        