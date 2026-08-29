class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l,r = 0, 0
        res = 0
        while r < len(s):
            if s[r] not in count:
                count[s[r]] = 1
            elif s[r] in count:
                count[s[r]] += 1
            # window sz - max char freq <= k
            if (r - l + 1) - max(count.values()) > k: # not enough replacements
                count[s[l]] -= 1
                l += 1
            if (r - l + 1) - max(count.values()) <= k:
                res = max(res, r - l + 1)
            r += 1
        return res