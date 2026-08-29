from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use hashmap get freq, 
        # loop through and return true if values > 1
        c = Counter(nums)
        for f in c.values():
            if f > 1:
                return True
        
        return False