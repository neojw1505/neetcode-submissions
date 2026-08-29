class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, path = [],[]
        count_map = Counter(nums)        
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return

            for n in count_map:
                if count_map[n] > 0:
                    path.append(n)
                    count_map[n] -= 1

                    backtrack()

                    path.pop()
                    count_map[n] += 1
        backtrack()
        return res