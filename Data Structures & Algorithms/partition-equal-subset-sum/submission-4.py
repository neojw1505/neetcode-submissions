class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False # odd value cannot be split evenly

        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            new_dp = set(dp)
            for t in dp:
                new_sum = t+nums[i]
                if new_sum == target:
                    return True
                elif new_sum < target:
                    new_dp.add(new_sum)
            dp = new_dp
        return False


            
