class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        length = 0
        l = 0
        for r,ch in enumerate(s):
            while ch in my_set:
                my_set.remove(s[l])
                l += 1
            my_set.add(ch)
            length = max(length, r - l + 1)
        return length
            