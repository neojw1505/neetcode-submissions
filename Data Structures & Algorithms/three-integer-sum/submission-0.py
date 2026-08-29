class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort first
        nums.sort()
        print(nums)
        res = []
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 2 sum
            L, R = i + 1, len(nums) - 1
            while L < R:
                # formula
                threeSum = a + nums[L] + nums[R]

                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    res.append([a, nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        return res
        