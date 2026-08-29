class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for n in nums:
            d[n] = 1 + d.get(n, 0)
        
        for k,v in d.items():
            if v > 1:
                return True
        return False