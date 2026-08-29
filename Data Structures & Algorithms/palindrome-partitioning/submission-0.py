class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []
        def isPali(substr):
            l,r = 0,len(substr)-1
            while l <= r:
                if substr[l] != substr[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        def backtrack(start):
            if len(''.join(path)) == len(s):
                res.append(path[:])
            
            for i in range(start, len(s)):
                substr = s[start: i+1]
                if isPali(substr):
                    path.append(substr)
                    backtrack(i+1)
                    path.pop()
        backtrack(0)
        return res
