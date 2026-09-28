class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort() # sort cookies size
        g.sort() # sort child greed

        i = 0
        j = 0
        count = 0
        
        while i < len(s) and j < len(g):
            if s[i] >= g[i]:
                count += 1
                j += 1
                i += 1
            else:
                i += 1 # look for bigger cookie
        return count