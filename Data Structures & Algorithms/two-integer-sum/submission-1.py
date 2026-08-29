class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create empty hashmap to store values visited
        m = {}
        for i,n in enumerate(nums):
            diff = target - n # check if this value found in map
            if diff not in m:
                # add to map, the visited num and its index
                m[n] = i
            else:
                # if found, return the indices that sum up to target
                return [m[diff], i]

        