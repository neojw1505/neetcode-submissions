class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        maxLength = 0
        i = 0
        while i < len(s):
            ch = s[i]
            if ch not in m:
                m[ch] = True
                i += 1
                maxLength = max(maxLength, len(m))
            else:
                maxLength = max(maxLength, len(m))
                m = {}
        return maxLength