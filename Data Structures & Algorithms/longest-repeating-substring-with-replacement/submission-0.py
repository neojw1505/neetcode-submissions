class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Condition: length of window - maxFreq > k => invalid window
        count = {}

        L,R = 0,0
        maxFreq = 0
        maxWindowSize = 0

        while R < len(s):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxFreq = max(maxFreq, count[s[R]])

            # as long as dont meet condition
            while (R - L + 1) - maxFreq > k:
                # move left ptr forward
                count[s[L]] -= 1
                L += 1
            maxWindowSize = max(maxWindowSize, R - L + 1)
            R += 1 # move to next element
        return maxWindowSize