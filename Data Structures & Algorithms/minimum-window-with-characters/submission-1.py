class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "":
            return ""
        
        haveMap, needMap = {}, {}
        for c in t:
            needMap[c] = 1 + needMap.get(c, 0)
        
        have, need = 0, len(needMap)
        res = [] # store index of valid window
        l = 0
        minLength = float('infinity')
        for r, ch in enumerate(s):
            haveMap[ch] = 1 + haveMap.get(ch, 0)

            # check if ch is inside needMap and freq same
            if ch in needMap and haveMap[ch] == needMap[ch]:
                have += 1

            # all conditions are met
            while have == need:
                # check valid window smaller than minLength
                if (r - l + 1) < minLength:
                    minLength = r - l + 1
                    res = [l, r]
                # check valid window but bigger than minLength
                else:
                    haveMap[s[l]] -= 1
                    if s[l] in needMap and haveMap[s[l]] < needMap[s[l]]:
                        have -= 1
                    l += 1
        return s[res[0]:res[1]+1] if minLength != float('infinity') else ""