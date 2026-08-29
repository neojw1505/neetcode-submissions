class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if length same
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        # can be s or t, they are same length
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # store in countS map 
            countT[t[i]] = 1 + countT.get(t[i], 0) # store in countT map 
        
        return countS == countT