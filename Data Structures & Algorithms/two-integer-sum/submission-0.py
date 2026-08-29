class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in s:
                if i > s[diff]:
                    return [s[diff], i]
                else:
                    return [i, s[diff]]
            s[nums[i]] = i

                