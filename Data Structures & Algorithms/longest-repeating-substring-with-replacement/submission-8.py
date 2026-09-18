class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        l,r = 0, 0
        longest = 0
        max_freq = 0
        while r < len(s):
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])
            if (r-l+1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
            r += 1
        return longest

# "XYYX"
# {X:2, Y:2} # longest=3 # r=1 # l=0 # n=4 