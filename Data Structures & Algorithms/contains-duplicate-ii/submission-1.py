class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in d:
                if i - d[nums[i]] <= k:
                    return True
            d[nums[i]] = i
        return False
    
        # d = {1:0, 2:1, 3:2}
        # i = 3 - 0  <= 3
        # T: O(n) S:O(unique nums but worse case is n)