class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Approach: expand from center checking the left and right char
        # need to account for Odd and Even strings, as each have diff center
        # need to rmb to bring the pointers back before returning the string
        # need to remeber r + 1, to include the char at r in the slice

        def expand(l,r):
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            l = l + 1
            r = r - 1
            return l,r

        start_index, end_index = 0,0 
        
        for i in range(len(s)):
            l1,r1 = expand(i,i)
            l2,r2 = expand(i,i+1)
            if (r1-l1) > (end_index-start_index):
                start_index, end_index = l1,r1
            if (r2-l2) > (end_index-start_index):
                start_index, end_index = l2,r2
        
        return s[start_index:end_index+1]

    # T:O(n^2) S:O(N)