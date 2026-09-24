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
            return s[l:r+1]

        longest_sub_str = ""
        for i in range(len(s)):
            sub_str1 = expand(i,i)
            sub_str2 = expand(i,i+1)
            if len(sub_str1) > len(longest_sub_str):
                longest_sub_str = sub_str1
            if len(sub_str2) > len(longest_sub_str):
                longest_sub_str = sub_str2
        
        return longest_sub_str