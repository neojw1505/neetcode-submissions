class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ = sum(nums)
        n = len(nums)
        expected_sum = 0
        for i in range(n+1):
            expected_sum += i
        return expected_sum - summ
