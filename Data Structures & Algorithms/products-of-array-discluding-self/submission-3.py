class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_count = 1
        left = [1]
        for i in range(len(nums)-1):
            left_count = left_count * nums[i]
            left.append(left_count)

        right_count = 1
        right = [1]
        for i in range(len(nums)-1, 0, -1):
            right_count = right_count * nums[i]
            right.append(right_count)
        right.reverse()
        
        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i])
        return res
