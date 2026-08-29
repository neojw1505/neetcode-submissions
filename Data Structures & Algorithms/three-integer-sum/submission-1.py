class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array 
        nums.sort()
        res = []
        # Formula: a + nums[l] + nums[r] == 0
        for i, a in enumerate(nums): 
            # needs to reset for each value of 'a'
            l, r = i + 1, len(nums) - 1
            # check a visited before
            if i > 0 and a == nums[i-1]:
                continue
            # 2 sum logic
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: 
                    r -= 1
                elif threeSum < 0: 
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                
        return res
                