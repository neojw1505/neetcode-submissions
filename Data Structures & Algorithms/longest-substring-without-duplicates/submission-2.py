class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        maxLength = 0
        tmp = 0
        for ch in s:
            if ch not in m:
                m[ch] = True
                tmp += 1
            else:
                maxLength = max(maxLength, tmp)
                tmp = 0
                del m[ch]
        return max(tmp, maxLength)