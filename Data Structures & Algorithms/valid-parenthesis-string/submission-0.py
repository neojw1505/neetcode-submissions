class Solution:
    def checkValidString(self, s: str) -> bool:
        d = Counter(s)
        print(d)

        wildCardNeeded = abs(d['('] - d[')'])

        if wildCardNeeded == 0 or d['*'] > wildCardNeeded: 
            return True
        else:
            return False
        