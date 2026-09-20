class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        maxLength = 0
        i = 0
        length = 0
        while i < len(s):
            ch = s[i]
            if ch not in m:
                m[ch] = True
                length += 1
                i += 1
            else:
                maxLength = max(maxLength, len(m))
                m = {}
        return max(maxLength, legnth)