class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]

        # detect the collision point
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # find entrance of cycle = duplicate num
        slow = 0 # reset
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow