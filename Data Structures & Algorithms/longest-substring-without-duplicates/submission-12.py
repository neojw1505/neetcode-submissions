class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set() # keep track of duplicates
        l = 0
        maxLength = 0
        for r, ch in enumerate(s):
            # as long as there is duplicate in the set
            # shrink window by pushing left pointer by 1
            while ch in my_set:
                # delete from set
                my_set.remove(s[l])
                # move left ptr by 1
                l += 1
            # no more duplicates
            my_set.add(ch)
            # compare maxLength with curr window size
            maxLength = max(maxLength, r - l + 1)
        return maxLength

